from flask import Blueprint # 引入蓝图模块

home_blue = Blueprint('home_blue',__name__) # 创建蓝图对象

from . import views # 从 home/views.py 中导入当前模块