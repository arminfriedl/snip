import os
import logging

from . import app

logger = logging.getLogger(__name__)

default_env = "local"

config_vars = [
    "SQLALCHEMY_DATABASE_URI",
    "SQLALCHEMY_TRACK_MODIFICATIONS",
    "SECRET_KEY",
    "DEBUG",
    "ENV"
]


def find_env():
    env = (os.environ.get("SNIP_ENV")
           or os.environ.get("FLASK_ENV")
           or default_env)

    if not env:
        raise Exception("Could not determine environment")

    logger.info(f"Using environment {env}")


def find_config_file(env):
    config_file = f"config.{env}.py"
    logger.info(f"Config file {config_file}")
    return config_file


def validate(config):
    key = config.get("SECRET_KEY")
    if isinstance(key, str):
        key = key.encode("utf-8")
    if not isinstance(key, bytes):
        raise Exception("Secret key cannot be cast to bytes")
    if len(key) < 64:  # for blake2b hashing in snipper
        raise Exception("Secret key must be 64 bytes long")

    logger.info("Configuration is valid")


def configure(env=None):
    logger.info("Configuring snip")
    if not env:
        env = find_env()
    app.config.from_pyfile(find_config_file(env))
    validate(app.config)
