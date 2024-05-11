from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField , DateField , RadioField
from wtforms.validators import DataRequired ,Email , EqualTo , ValidationError
from flask_wtf.file import FileField, FileAllowed
from src import db
import sqlalchemy as sa
from src.models import User

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
    username = StringField('Username', validators=[DataRequired()],render_kw={"placeholder": "User name"})
    email = StringField('Email', validators=[DataRequired(), Email(message='Invalid email')],render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired()] ,render_kw={"placeholder": "Password"})
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')],render_kw={"placeholder": "Repeat Password"})
    firstname = StringField('Username', validators=[DataRequired()],render_kw={"placeholder": "First Name"})
    lastname = StringField('Username', validators=[DataRequired()],render_kw={"placeholder": "Last Name"})
    choices = [(1, 'Male'), (0, 'Female')]
    gender = RadioField('gender' ,choices=choices , validators=[DataRequired()] ) 
    birthdate = DateField('birth date' , validators=[DataRequired()])
    toggle = BooleanField('Join a Family')
    family_id = StringField('Family ID', render_kw={"style": "display: none;", "placeholder": "Family ID"})
    submit_signup = SubmitField('Sign Up')
    
    
    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')
    
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

    
    




    
    

    
    
    
    
        

    

    
    
