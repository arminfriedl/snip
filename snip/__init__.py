import os
from flask import Flask


###########################
# Read snip configuration #
###########################
from . import config
snip_config = config.configure()


###############
# Setup Flask #
###############

# ENV and DEBUG are special in flask. They must be set to the environment before app init.
# https://flask.palletsprojects.com/en/1.1.x/config/#environment-and-debug-features
os.environ['FLASK_ENV'] = snip_config.SNIP_FLASK_ENVIRONMENT
os.environ['FLASK_DEBUG'] = str(snip_config.SNIP_FLASK_DEBUG)
# FLASK_SKIP_DOTENV currently only read from environment
os.environ['FLASK_SKIP_DOTENV'] = str(snip_config.SNIP_FLASK_SKIP_DOTENV)

app = Flask(__name__)

app.config.update(
    SECRET_KEY                     = snip_config.SNIP_FLASK_SECRET.get_secret_value(),
    PREFERRED_URL_SCHEME           = snip_config.SNIP_FLASK_PREFERRED_URL_SCHEME,
    SQLALCHEMY_DATABASE_URI        = snip_config.SNIP_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS = snip_config.SNIP_DATABASE_TRACK_MODIFICATION)


###################
# Setup SQAlchemy #
###################
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from . import models
db.create_all()


##############
# Setup snip #
##############
from . import api
from . import views
