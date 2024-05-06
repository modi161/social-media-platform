from flask import render_template , redirect ,request , flash

from src import app,db
import sqlalchemy as sa
from src.models import User
from src.models import Content, ContentPhotos, Family, FamilyFollowing


@app.route('/')
def start_page():
    return render_template('index.html')

@app.route('/user/<username>')
# login_required should be added here ////////////////////
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username)) #will trigger a 404 error if user not found in the db
    return render_template('profile.html' , user = user)

@app.route('/feedpage/<username>')
# show the posts
def feedPage(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    family_id = user.FamilyID
    
    families = Family.query.filter(Family.id != family_id).all()


    TableOfContent = db.session.query(Family, FamilyFollowing, User, Content, ContentPhotos).\
        join(FamilyFollowing, Family.id == FamilyFollowing.FollowingFamilyId).\
        join(User, User.FamilyID == FamilyFollowing.FollowedFamilyId).\
        join(Content, User.id == Content.userId).\
        join(ContentPhotos, Content.id == ContentPhotos.contentId).all()
    
    posts = [row for row in TableOfContent if row[0].id == family_id]
    print(families)

    return render_template('homefeed.html', User = user, Posts=posts, Families = families)
    #User=user, Disp=DispContent, 

#post it to the backend




