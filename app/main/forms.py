from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, FileField, SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yo.. self.', validators=[Required()])
    submit = SubmitField('submit')


class UpdatePitch(FlaskForm):
    title = StringField("TITLE PITCH", validators=[Required()])
    pitch = TextAreaField("PITCHES", validators=[Required()])
    category = SelectField("CATEGORY", choices=[("General", "General"), (
        "Leadership", "Leadership"), ("Justice", "Justice"), ("Hope", "Hope")])

    submit = SubmitField("Add Pitch")


class CommentForm(FlaskForm):
    comment = TextAreaField(
        "Feel free to comment on any CATEGORY", [Required()])
    submit = SubmitField("Submit")

    # justice# The deceitful have no friends
    # Leadership#A gentle hand may lead even an elephant by a hair
    # general#An army of a thousand  is easy to find ah how difficult to find
    # a general!!
    # Hope# We must accept finite disappointemnt, but never lose infinite hope.
