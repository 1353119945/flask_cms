class Config:
    DEBUG = None

    #配置数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:abc123456@127.0.0.1:3306/cms' # 连接数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

# 定义开发模式的配置
class developmentConfig(Config):
    DEBUG = True    #由于上面入口文件读取的是开发环境的 DEBUG，我们设置的是 true，所以Debugger显示的是 active。如果改成 production，你会看到 DEBUG 为 off的状态

# 定义生产模式的配置
class productionConfig(Config):
    DEBUG = True

# 定义字典，方便取值
config = {
    'development' : developmentConfig,
    'production' : productionConfig
}