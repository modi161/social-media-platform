from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired 
from flask_wtf.file import FileField, FileAllowed

class editform(FlaskForm):
    bio = TextAreaField('Bio')
    cover_photo = FileField('Cover Photo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    profile_photo = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Save')

 
    
    




    
    

    
    
    
    
        

    

    
    
