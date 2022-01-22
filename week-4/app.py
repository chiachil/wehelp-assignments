# 載入flask工具
from flask import Flask
from blueprint import blueprint

# 初始化flask物件
app=Flask(__name__)
app.register_blueprint(blueprint)

# session密鑰
app.secret_key = "k_ih5metrfv"

app.run(port=3000)