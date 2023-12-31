from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, validators, EqualTo
from wtforms.validators import DataRequired, Email, Length


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class UserEditForm(FlaskForm):
    """Form to edit a user"""

    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Password", validators=[DataRequired(), Email()])
    image_url = StringField("(Optional) Image URL")
    header_img_url = StringField("(Optional) Image Header URL")
    bio = TextAreaField("Bio", Length(max=150))
    password = PasswordField("Confirm Password", 
                             validators=[DataRequired(), Length(min=6)])
