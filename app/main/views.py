from flask import render_template,request,redirect,url_for,abort
from . import main
from app import create_app
from ..models import User
from .forms import UpdateProfile
from flask_login import login_required, current_user
from .. import db,photos