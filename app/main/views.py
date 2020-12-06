
from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment
from .forms import updateProfile,PitchForm,CommentForm
from .. import db,photos
from flask_login import login_required,current_user

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id).all()
    if user is None:
        abort(404)

    return render_template('profile/profile.html',user = user,pitches=pitches)   

