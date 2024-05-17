from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField , DateField , RadioField ,IntegerField, SelectField
from wtforms.validators import DataRequired ,Email , EqualTo , ValidationError
from flask_wtf.file import FileField, FileAllowed
from src import db
import sqlalchemy as sa
from src.models import User,Family

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
        
    # def validate_family_id(self, family_id):
    #     family = db.session.scalar(sa.select(Family).where(
    #         Family.id == family_id.data))
    #     if family is not None:
    #         raise ValidationError('There is no family with this id')
    
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

class EditContentForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    contentID =  IntegerField("Type", validators=[DataRequired()])
    # visibility =  IntegerField("Visibility",validators=[DataRequired()])
    visibility = SelectField('Visibility', choices=[('1', 'Public'), ('0', 'Private')], validators=[DataRequired()])
    image = FileField("Image")  
    submit2 = SubmitField("Update")

    
    
class CreateFamilyForm(FlaskForm):
    familyname = StringField('Family Name', id='family-name', render_kw={"class": "family_name","placeholder": "Family Name"}, 
                              validators=[DataRequired()], description="Family Name")
    bio = StringField('bio', validators=[DataRequired()],
                      id='family-bio',
                      render_kw={"placeholder": "what is the best thing in you as a family?","class": "family_bio"})
    
    family_profile_input = FileField('family_profile_input',   id = 'family-profile-input')
    
    family_cover_input = FileField('family_cover_input', id='family-cover-input')
    
    createfam = SubmitField('Create Family' ,id='submit-button' ,render_kw={"class": "btn btn-primary"})
    


class FollowForm(FlaskForm):
    followedFamily = IntegerField("Followed", validators=[DataRequired()])
    submit1 = SubmitField("Follow")

    
    
class UnfollowForm(FlaskForm):
    FamilyId = IntegerField("Id", validators=[DataRequired()])
    submit3 = SubmitField("unfollow")
    

    
    
