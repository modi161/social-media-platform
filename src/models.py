# models.py
# importing the db instanse
from . import db

from typing import Optional
from sqlalchemy import Integer , String , Boolean , Date , ForeignKey ,Text
from sqlalchemy.orm import Mapped , mapped_column
#from src import db
from datetime import datetime,timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from src import login


class  Family(db.Model):
    __tablename__ ="family"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    
    familyname : Mapped[str] = mapped_column(String(80) , unique=True ,nullable=False)
    
    bio : Mapped[Optional[str]] = mapped_column(Text)
    
    creationdate : Mapped[datetime] = mapped_column(index=True , default=lambda: datetime.now(timezone.utc))
    
    coverphoto : Mapped[str] = mapped_column(String(250))
    
    profilephoto : Mapped[str] = mapped_column(String(250))


class User(db.Model,UserMixin):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    username: Mapped[str] = mapped_column(String(60) , index=True , unique=True , nullable=False)
    
    FirstName: Mapped[str] = mapped_column(String(80) , nullable=False)
    
    email: Mapped[str] = mapped_column(String(150), unique=True , index=True ,nullable=False)
    
    password_hash: Mapped[Optional[str]] = mapped_column(String(256))
    
    lastname: Mapped[str] = mapped_column(String(80) , nullable=False )
    
    
    #1=male 0=female
    Gender : Mapped[bool] = mapped_column(Boolean , nullable= False)
    
    Birthdate : Mapped[Date] = mapped_column(Date , nullable=False)
    
    FamilyID : Mapped[int] = mapped_column(ForeignKey(Family.id), nullable=False ,index=True)

    
    # 1 = admin 0 = normal member
    FamilyRole : Mapped[bool] = mapped_column(Boolean ,nullable=False)
    
    bio : Mapped[Optional[str]] = mapped_column(Text)
    photo : Mapped[str] = mapped_column(String(250))
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
    
    
class Content(db.Model):
    __tablename__ = "content"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    
    description : Mapped[str] = mapped_column(Text)
    
    timestamp : Mapped[datetime] = mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    
    # 1 = visibale 0 = not visibale
    visibility : Mapped[bool] = mapped_column(Boolean , nullable=False)
    
    #1 = post , 2 = album
    Type : Mapped[bool] = mapped_column(Boolean , nullable=False)
    
    userId : Mapped[int] = mapped_column(ForeignKey(User.id) ,index=True ,nullable=False)
    
    
    

class ContentPhotos(db.Model):
    __tablename__ = "contentphotos"
    
    contentId : Mapped[int] = mapped_column(ForeignKey(Content.id) , primary_key=True)
    
    photoUrl : Mapped[str] = mapped_column(String(250),primary_key=True ,nullable=False)





class UserLikedContent(db.Model):
    __tablename__ = "UserLikedContent"
    
    UserId : Mapped[int] = mapped_column(ForeignKey(User.id) , primary_key=True)
    
    ContentId : Mapped[int] = mapped_column(ForeignKey(Content.id) , primary_key=True)
    
    
    

class FamilyFollowing(db.Model):
    __tablename__ = "FamilyFollowing"
    
    FollowingFamilyId : Mapped[int] = mapped_column(ForeignKey(Family.id) , primary_key=True)
    
    FollowedFamilyId : Mapped[int] = mapped_column(ForeignKey(Family.id) , primary_key=True)
    
    
    

class FamilyPendingRequests(db.Model):
    __tablename__ = "FamilyPendingRequests"
    
    UserId : Mapped[int] = mapped_column(ForeignKey(User.id) ,primary_key=True)
    
    FamilyId : Mapped[int] = mapped_column(nullable=False)