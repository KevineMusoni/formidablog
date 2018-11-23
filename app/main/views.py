from flask import render_template,request,redirect,url_for,abort
from app import create_app
from . import main
from ..models import Comment, User
from .forms import CommentForm,UpdateProfile
from flask_loginuired, current_user
from .. import db,photos
import markdown2

@main.route('/')
def index()
title ='Home - Welcome to Formidablog'
return render_template('index.html')

@main.route('/blog/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    blog = get_blog(id)

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        new_comment =(blog_id=blog.id, blog_title=title,blog_comment=comment, user=current_user)
        new_comment.save_comment()
        return redirect(url_for('.blog', id=blog.id))

    title = f'{blog.title} comment'
    return render_template('new_comment.html', title=title, comment_form=form, blog=blog)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@login_required
@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
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

@main.route('/comment/<int:id>')
def single_comment(id):
    comment = Comment.query.get(id)
    if comment is None:
        abort(404)
    format_comment = markdown2.markdown(comment.blog_comment, extras=["code-friendly", "fenced-code-blocks"])
    return render_template('comment.html', comment=comment, format_comment=format_comment)
