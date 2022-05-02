from flask_script import Manager # 导入扩展，用于管理器启动项目
from flask_migrate import Migrate,MigrateCommand # 导入迁移包

from app import create_app,db # 导入工厂函数create_app和db函数

app = create_app("development") # 调用函数，获取实例，这里使用的是开发模式的app

manage = Manager(app) # 实例化管理器
Migrate(app,db) # 注入框架实例和数据实例
manage.add_command('db',MigrateCommand) # 添加迁移命令

@app.route('/')
def index():
    return 'hello HLB!'

if __name__ == '__main__':
    manage.run()    #对应实例manage（没有实例化就是app.run() ）