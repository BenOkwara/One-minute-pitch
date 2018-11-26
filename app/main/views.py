from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from . forms import UpdateProfile, UpdatePitch, CommentForm
from app.models import User, Pitch, Comment
from . import main
from .. import db


@main.route('/')
def index():

    # profile = profile
    pitchs = Pitch.query.all()
    title = 'Got a Pitch ..?'
    return render_template('index.html', title = title, pitchs = pitchs)


@main.route('/pitch/new', methods=['GET', 'POST'])
@login_required
def add_pitch():
    form = UpdatePitch()
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        posted = form.category.data

        # Update pitch instance
        new_pitch = Pitch(title=title, description=pitch,
                          category=category, posted=posted, user=current_user)
        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New Pitch'
    return render_template('add_pitch.html', title=title, form=form)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    pitches = Pitch.query.filter_by(user_id=user.id).all()
    return render_template("index.html", user=user, pitches=pitches)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', uname=user.username))
    return render_template('profile/update.html', form=form)


@main.route('/pitches/<category>')
def get_pitches(category):

    pitches = Pitch.get_pitches(category)
    return render_template("index.html", pitches=pitches)


@main.route('/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def add_comment(id):
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data
        comment = Comment(comment=comment, pitch_id=id)

        # let's save the comments
        db.session.add(comment)
        db.session.commit()

        comment = Comment.query.filter_by(pitch_id=id).all()
    return render_template('comment.html', comment=comment, comment_form=form, post='New Comment')
