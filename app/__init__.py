from flask import Flask

from app.db import close_db, init_db


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev-secret-key-change-me",
        DATABASE=app.instance_path + "/auth.db",
    )

    # Garantir que a pasta instance exista para o SQLite.
    import os

    os.makedirs(app.instance_path, exist_ok=True)

    with app.app_context():
        init_db()

    from app.routes.auth import auth_bp

    app.register_blueprint(auth_bp)

    app.teardown_appcontext(close_db)

    return app
