from flask import Flask
from config import config #导入配置信息
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app) # 注册数据库实例,为app绑定配置，创建SQLAchemy对象

# 定义工厂函数，生产app
def create_app(config_name): # 传入要生产的模式参数：可以是开发模式的app，也可以是生产模式的app
    app.config.from_object(config[config_name])  # 使用配置
    db.init_app(app) # 通过 init_app 用来实例化db对象
    return app # 最后返回当前app