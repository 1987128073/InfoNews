from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import Redis


# 定义全局变量, 记录数据库连接对象, 以便其他文件可以使用
from config import config

db = None  # type: SQLAlchemy
rs = None  # type: Redis


def create_app(config_type):

    config_type = config[config_type]
    # 创建web应用
    app = Flask(__name__)
    # 从对象中加载配置
    app.config.from_object(config_type)
    # 定义全局变量
    global db, rs
    # 创建msql连接对象
    db = SQLAlchemy(app)
    # 创建redis连接对象
    rs = Redis(host=config_type.REDIS_HOST, port=config_type.REDIS_PORT)
    # 初始化Session对象
    Session(app)
    # 初始化迁移器
    Migrate(app, db)

    # 注册蓝图
    from info.home import home_blue  # 为了避免导入错误, 对于只使用一次的内容, 在使用前才导入
    app.register_blueprint(home_blue)

    return app
