# from flask import session # 引入flask自带的session

from flask import render_template # 引入模板包
from . import home_blue # 从home/__init__.py中导入蓝图对象

@home_blue.route('/')
def index():
    # session['name'] = 'HLB' # 删除这行代码，仅用于测试session
    return render_template('home/index/index.html') # 加载前台首页