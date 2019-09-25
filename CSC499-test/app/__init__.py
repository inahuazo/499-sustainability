# app/__init__.py
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

# Initialize app
app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

from app import routes 