from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired ,Email
from flask_wtf.file import FileField, FileAllowed

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
    
    




    
    

    
    
    
    
        

    

    
    
