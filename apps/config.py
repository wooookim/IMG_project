from pathlib import Path

basedir = Path(__file__).parent.parent


class BaseConfig:
    SECRET_KEY = "IMGPROJECT"
    WTF_CSRF_SECRET_KEY = "IMGPROJECTCSRF"


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:////{basedir / 'local.sqlite'}"  # db 제품 연결 제품 설정
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 경고 무시
    SQLALCHEMY_ECHO = True  # 콘솔에서 작동 상태 출력


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:////{basedir / 'testing.sqlite'}"  # db 제품 연결 제품 설정
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 경고 무시
    WTF_CSRF_ENABLED = False  # 테스트에서는 csrf 무효로 작동


config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}
