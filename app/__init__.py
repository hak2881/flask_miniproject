from config import db
from flask import Flask
from flask_migrate import Migrate

import app.models


migrate = Migrate()


def create_app():
    application = Flask(__name__)

    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    db.init_app(application)

    migrate.init_app(application, db)

    # 블루 프린트 등록
    from views.questions import question_blp
    from views.images import image_blp
    from views.choices import choices_blp
    
    application.register_blueprint(question_blp)
    application.register_blueprint(image_blp)
    application.register_blueprint(choices_blp)

    return application
