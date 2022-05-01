class Config:
    DEBUG = None

# 定义开发模式的配置
class developmentConfig(Config):
    DEBUG = True

# 定义生产模式的配置
class productionConfig(Config):
    DEBUG = True

# 定义字典，方便取值
config = {
    'development' : developmentConfig,
    'production' : productionConfig
}