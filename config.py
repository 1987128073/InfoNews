
# 定义配置类来封装配置信息
from datetime import timedelta

from redis import Redis


class Config:
    DEBUG = True  # 设置调试模式
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/infonews"  # 数据库连接地址
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 是否追踪数据库变化
    REDIS_HOST = "127.0.0.1"  # redis的连接地址  将自定义的配置也封装到Config类中
    REDIS_PORT = 6379
    SESSION_TYPE = "redis"  # 设置session存储的方式  redis 性能好,方便设置过期时间
    SESSION_REDIS = Redis(host=REDIS_HOST, port=REDIS_PORT)  # 设置Redis连接对象, 组件会使用该对象将session数据保存到redis中
    SESSION_USE_SIGNER = True  # 设置sessionid进行加密
    SECRET_KEY = "test"  # 设置sessionid的秘钥
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)  # 设置session过期时间 组件默认支持设置过期时间


# 配置信息子类化
class DevelopmentConfig(Config):  # 开发环境配置信息
    DEBUG = True  # 设置调试模式


class ProductionConfig(Config):  # 生产环境配置信息
    DEBUG = False


config = {'dev': DevelopmentConfig, 'pro': ProductionConfig}