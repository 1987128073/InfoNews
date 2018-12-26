from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

from config import DevelopmentConfig


def create_app():
    app = Flask(__name__)

    # 从对象中加载配置
    app.config.from_object(DevelopmentConfig)
    # 创建msql连接对象
    db = SQLAlchemy(app)
    # 创建redis连接对象
    rs = Redis(host=DevelopmentConfig.REDIS_HOST, port=DevelopmentConfig.REDIS_PORT)
    # 初始化Session对象
    Session(app)
    # 初始化迁移器
    Migrate(app, db)

    return app
