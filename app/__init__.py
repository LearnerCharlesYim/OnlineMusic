# _*_ Coding:utf-8 _*_

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    # 注册蓝图
    from app.home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    return app





