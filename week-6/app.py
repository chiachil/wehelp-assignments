# 載入flask工具,驅動mysql工具,環境配置套件
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

# 連接資料庫和建立緩衝游標
db = mysql.connector.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    port = os.getenv('DB_PORT'),
    password = os.getenv('DB_PASSWORD'),
    database = os.getenv('DB_NAME')
)
cursor = db.cursor(buffered=True)

# 初始化flask和設定session密鑰
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# 首頁
@app.route("/")
def index():
    return render_template("index.html")

# 註冊
@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    if name == "" or username == "" or password == "":
        return redirect(url_for("error", message = "姓名、帳號和密碼任一不能為空"))
    else:
        sql = "SELECT username FROM member WHERE username = '%s'" %username
        cursor.execute(sql)
        data = cursor.fetchone()
        # return "%s" % data 檢驗fetchone結果
        if not data == None:
            return redirect(url_for("error", message = "帳號已經被註冊"))
        else:
            sql = "INSERT INTO member (name,username,password) VALUES ('%s', '%s', '%s')" % (
                name, username, password)
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return redirect(url_for("index"))

#登入
@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username == "" or password == "":
        return redirect(url_for("error", message = "帳號和密碼任一不能為空"))
    else:
        sql = "SELECT name,username,password FROM member WHERE username = '%s' AND password = '%s'" % (username,password)
        cursor.execute(sql)
        data = cursor.fetchall()
        # return "%s" % data 檢驗fetchall結果
        if not data == []:
            session["username"] = username
            name = data[0][0]
            return redirect(url_for("member", name = "%s" % name))
        else:
            cursor.close()
            db.close()
            return redirect(url_for("error", message = "帳號或密碼輸入錯誤"))


@app.route("/member/")
def member():
    if "username" in session:
        name = request.args.get("name", "")
        return render_template("member.html",name = name)
    else:
        return render_template("index.html")

@app.route("/signout")
def signout():
    session.pop("username", "")
    return redirect(url_for("index"))


@app.route("/error/")
def error():
    error = request.args.get("message", "")
    return render_template("error.html", message = error)

# 判斷執行非當作引入模組
if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)