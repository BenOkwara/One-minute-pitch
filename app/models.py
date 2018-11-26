from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    pitches = db.relationship('Pitch', backref = 'user', lazy = 'dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You just Entered wrong Password')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

class Pitch(db.Model):
    __tablename__= 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    category = db.Column(db.String(255))
    comments = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,categories):
        pitches = Pitch.query.filter_by(categories = categories).all()
        return pitches

    @classmethod
    def get_pitch(cls,id):
        pitch = Pitch.query.filter_by(id = id).first()
        return pitch

    @classmethod
    def pitch_count(cls,uname):
        user = User.db.query.filter_by(username = uname).first()
        pitches = Pitch.query.filter_by(user_id = user.id).all()

        pitch_count = 0
        for pitch_count in pitches:
            pitch_count +=1
        return pitch_count

    def get_comments(self):
        pitch = Pitch.query.filter_by(id = self.id).first()
        comments = Comment.query.filter_by(pitch_id = pitch.id).all()
        return comments

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    name =db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))
    posted = db.Column(db.DateTime, default = datetime.utcnow)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User{self.comment}'
