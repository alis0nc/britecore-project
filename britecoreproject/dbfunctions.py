"""Database functions."""
from britecoreproject import app, orm
from sqlobject import *

def connect_db():
    """Connects to the specific database."""
    sqlhub.processConnection = connectionForURI(app.config['DATABASE'])

def init_db():
    """Initialises the database."""
    db = get_db()
    orm.create_tables()

def get_db():
    """Opens a new database connection if there is none yet for the 
    current application context."""
    if not hasattr(sqlhub, 'processConnection'):
        connect_db()
    return sqlhub.processConnection
