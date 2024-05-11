from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField,FileField
from wtforms.validators import DataRequired ,Email
from flask_wtf.file import FileField, FileAllowed
import os

class Editform(FlaskForm):
    bio = TextAreaField('Bio')
    cover_photo = FileField('Cover Photo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    profile_photo = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Save')

 
class Loginform(FlaskForm):
    email = StringField('Email', validators=[DataRequired()],render_kw={"placeholder": "Email"})
    password = PasswordField('Password' , validators=[DataRequired()],render_kw={"placeholder": "Password"}) 
    log = SubmitField('Login')
    
    
    
class Signupform(FlaskForm):
    username = StringField('Username', validators=[DataRequired()],render_kw={"placeholder": "Name"})
    email = StringField('Email', validators=[DataRequired(), Email(message='Invalid email')],render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder": "Password"})
    toggle = BooleanField('Join a Family')
    family_id = StringField('Family ID', render_kw={"style": "display: none;", "placeholder": "Family ID"})
    submit = SubmitField('Sign Up')
    pass    
    
class ContentForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()], render_kw={"placeholder": "What is on your mind"})
    visibility =  IntegerField("Visibility",validators=[DataRequired()])
    type =  IntegerField("Type", validators=[DataRequired()])
    userID =  IntegerField("Type", validators=[DataRequired()])
    postImage = FileField("Image")  
    albumImage = FileField("Image")  
    submit = SubmitField("Submit")
    
class DeleteContentForm(FlaskForm):
    contentID =  IntegerField("Type", validators=[DataRequired()])
    submit = SubmitField("Submit")

class FollowForm(FlaskForm):
    followedFamily = IntegerField("Followed", validators=[DataRequired()])
    submit = SubmitField("Follow")


class LikeForm(FlaskForm):
    ContentId = IntegerField("Id", validators=[DataRequired()])
    submit1 = SubmitField(" ")
    

class UnlikeForm(FlaskForm):
    ContentId = IntegerField("Id", validators=[DataRequired()])
    submit2 = SubmitField(" ")
    
    
class UnfollowForm(FlaskForm):
    FamilyId = IntegerField("Id", validators=[DataRequired()])
    submit3 = SubmitField("unfollow")
    

    
    
