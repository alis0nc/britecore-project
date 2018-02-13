"""Configuration."""
from britecoreproject import app

# load config from this very file
app.config.from_object(__name__)
# load some reasonable defaults
app.config.update(dict(
    DATABASE='sqlite:/:memory:'
))
# and overrides from an environment variable
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
