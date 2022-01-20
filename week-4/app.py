# 載入flask工具
from flask import Flask, redirect, render_template, request, session

# 初始化flask物件
app=Flask(
    __name__
)

# session密鑰
app.secret_key = "k_ih5metrfv"

# 首頁 "/"
@app.route("/")
def index():
    return render_template("index.html")

# 登入驗證頁面 "/signin"
@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    if account == "" or password == "":
        return redirect("/error/?message=請輸入帳號、密碼")
    elif account == "test" and password == "test":
        session["user_id"] = account  # 建立session，為已登入狀態
        return redirect("/member/")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")

# 登入成功頁 "/member/"
@app.route("/member/")
def signin_success():
    if "user_id" in session: # 取session，檢查登入狀態
        return render_template("member.html")
    else:
        return render_template("index.html")

# 登入失敗頁 "/error/"
@app.route("/error/")
def signin_error():
    error = request.args.get("message", "")
    return render_template("error.html", message = error)

# 登出功能頁 "/signout"
@app.route("/signout")
def signout():
    session.pop("user_id", "")  # 跳出session，為未登入狀態
    return redirect("/")



app.run(port=3000)