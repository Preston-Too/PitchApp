
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


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = updateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
           
        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)  

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/pitch/newpitch',methods= ['POST','GET'])
@login_required
def newPitch():
    pitch = PitchForm()
    if pitch.validate_on_submit():
        title = pitch.pitch_title.data
        category = pitch.pitch_category.data
        yourPitch = pitch.pitch_comment.data


        newPitch = Pitch(pitch_title = title,pitch_category = category,pitch_comment = yourPitch,user= current_user)

        #save pitch
        newPitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'NEW PITCH'
    return render_template('newPitch.html',title = title,pitchform = pitch)  