from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import config

db = SQLAlchemy()
csrf = CSRFProtect()


def create_app(config_key):
    app = Flask(__name__)

    """
    # config 파일 분리
    app.config.from_mapping(
        SECRET_KEY="IMGPROJECT",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",  # db 제품 연결 제품 설정
        SQLALCHEMY_TRACK_MODIFICATIONS=False,  # 경고 무시
        SQLALCHEMY_ECHO=True,  # 콘솔에서 작동 상태 출력
    )
    """
    app.config.from_object(config[config_key])

    csrf.init_app(app)
    db.init_app(app)
    Migrate(app, db)

    from crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app
