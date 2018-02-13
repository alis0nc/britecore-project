"""
# britecoreproject

Product Development project for the BriteCore interview process
:copyright: 2018 Alison Chan <alisonc@alisonc.net>
:license: MIT; see LICENSE for details
"""

from sqlobject import *
from flask import *
app = Flask(__name__)

import britecoreproject.config
import britecoreproject.views