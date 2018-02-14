"""Configuration."""
from britecoreproject import app

# load config from this very file
app.config.from_object(__name__)
# load some reasonable defaults
app.config.update(dict(
    DATABASE='sqlite:///home/alisonc/Code/britecore-project/sample.sqlite3'
))
# and overrides from an environment variable
app.config.from_envvar('BRITECORE_RISKS_SETTINGS', silent=True)
