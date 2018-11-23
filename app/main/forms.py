from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):
 title = StringField('Comment title', validators=[Required()])

 comment = TextAreaField('Blog comment')

 submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Whats on your mind?',validators = [Required()])
    submit = SubmitField('Submit')
