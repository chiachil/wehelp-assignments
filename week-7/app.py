# 載入flask工具,驅動mysql工具,環境配置套件
from urllib import response
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

# 初始化flask和設定session密鑰
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# 開啟一個共用的資料庫連線
connection = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    port=os.getenv('DB_PORT'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

# 首頁
@app.route("/")
def index():
    return render_template("index.html")

# 註冊功能
@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    if name == "" or username == "" or password == "":
        return redirect(url_for("error", message = "姓名、帳號和密碼任一不能為空"))
    cursor = connection.cursor(buffered=True)
    # 改用 cursor.execute() 的第二個參數來帶入變數資料到 SQL 語句，預防SQL Injection
    cursor.execute("SELECT username FROM member WHERE username = %s", (username,))
    data = cursor.fetchone()
    if data:
        cursor.close()
        print(data)
        return redirect(url_for("error", message = "帳號已經被註冊"))
    sql = "INSERT INTO member (name,username,password) VALUES (%(name)s, %(username)s, %(password)s)"
    # 以字典型態傳遞參數，確保多個參數的順序正確
    params = {"name": name, "username": username, "password": password}
    cursor.execute(sql,params)
    connection.commit()
    cursor.close()
    return redirect(url_for("index"))

# 登入功能
@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username == "" or password == "":
        return redirect(url_for("error", message = "帳號和密碼任一不能為空"))
    sql = "SELECT name,username,password FROM member WHERE username = %(username)s AND password = %(password)s"
    params = {"username": username,"password": password}
    cursor = connection.cursor(buffered=True)
    cursor.execute(sql,params)
    data = cursor.fetchall()
    if data:
        session["username"] = username
        name = data[0][0]
        cursor.close()
        return redirect(url_for("member", name = name))
    return redirect(url_for("error", message = "帳號或密碼輸入錯誤"))

# 會員頁
@app.route("/member/")
def member():
    if "username" in session:
        name = request.args.get("name", "")
        return render_template("member.html",name = name)
    return render_template("index.html")

# 登出功能
@app.route("/signout")
def signout():
    session.pop("username", "")
    return redirect(url_for("index"))

# 錯誤頁
@app.route("/error/")
def error():
    error = request.args.get("message", "")
    return render_template("error.html", message = error)

# 查詢會員功能api
@app.route("/api/members", methods=['GET'])
def getMember():
    username = request.args.get("username", "")
    cursor = connection.cursor(buffered=True)
    cursor.execute("SELECT id,name,username FROM member WHERE username= %s", (username,))
    cursor.close
    # 產出資料庫欄位名稱
    field_name = [i[0] for i in cursor.description]
    # fetch結果為列表或null
    result = cursor.fetchone()
    if result:
        content = dict(zip(field_name, result))
        print(content)
        return jsonify({"data":content})
    return jsonify({"data": result})

# 判斷執行非當作引入模組
if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)