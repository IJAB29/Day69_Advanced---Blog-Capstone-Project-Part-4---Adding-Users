from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, InputRequired, Email, Length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[InputRequired()])
    subtitle = StringField("Subtitle", validators=[InputRequired()])
    img_url = StringField("Blog Image URL", validators=[
                          InputRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[InputRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[
        InputRequired(),
    ])
    email = StringField("Email", validators=[
        InputRequired(),
        Email()
    ])
    password = PasswordField("Password", validators=[
        InputRequired(),
        Length(min=8, max=16)
    ])
    submit = SubmitField()


# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        InputRequired(),
        Email()
    ])
    password = PasswordField("Password", validators=[
        InputRequired()
    ])
    submit = SubmitField()


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[
        InputRequired()
    ])
    submit = SubmitField("Comment")
