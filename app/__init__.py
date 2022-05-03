from flask import Flask
from config import config #导入配置信息
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
from flask_session import Session # 导入session扩展
=======
from flask_session import Session
>>>>>>> temp

app = Flask(__name__)
db = SQLAlchemy(app) # 注册数据库实例,为app绑定配置，创建SQLAchemy对象

# 定义工厂函数，生产app
def create_app(config_name): # 传入要生产的模式参数：可以是开发模式的app，也可以是生产模式的app
<<<<<<< HEAD
    app.config.from_object(config[config_name])  # 使用配置

    db.init_app(app) # 通过 init_app 用来实例化db对象
    Session(app) # 实例化Session
=======
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 使用配置

    db.init_app(app) # 通过 init_app 用来实例化db对象
    Session(app)

    #注册前台蓝图
    from app.home import home_blue
    app.register_blueprint(home_blue)
>>>>>>> temp

    return app # 最后返回当前app