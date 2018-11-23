from flask import Blueprint
from flask_login import LoginManager
main = Blueprint('main',__name__)
from . import views,error
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
