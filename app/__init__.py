from flask import Flask
from flask_cors import CORS
from config import Config
from .routes.api import api
from .routes.errors import errors

app = Flask(__name__)
app.config.from_object(Config)
CORS(api, origins="*")

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(errors, url_prefix="/")

