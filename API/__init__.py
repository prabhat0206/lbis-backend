from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail

app = Flask(__name__, template_folder="../templates")
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)
CORS(app)


db.init_app(app)
migrate.init_app(app, db)


def get_model_dict(model):
    return dict((column.name, getattr(model, column.name))
                for column in model.__table__.columns)


from .public import public_api
from .admin import admin_api

app.register_blueprint(public_api, url_prefix="/api")
app.register_blueprint(admin_api, url_prefix="/admin")


