from flask import Flask
from flask_script import Manager # 导入扩展，用于管理器启动项目

app = Flask(__name__)
manage = Manager(app) # 实例化管理器

@app.route('/')
def index():
    return 'hello HLB!'

if __name__ == '__main__':
    manage.run()    #对应实例manage（没有实例化就是app.run() ）