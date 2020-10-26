from flask import Flask

app = Flask(__name__)

from . import config
config.configure("local")

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from . import models
from . import api
from . import views
