from . import app
from . import snip_config

if __name__ == "__main__":
    app.run(host=snip_config.SNIP_FLASK_HOST, port=snip_config.SNIP_FLASK_PORT)
