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
    user_family = Family.query.filter_by(id = user.FamilyID).first()
    #print(user_family.familyname)
    return render_template('profile.html' , user = user , user_family = user_family)

@app.route('/feedpage/<username>')
# show the posts
def feedPage(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    user_id = 1
    family_id = 1
    #query(User, Post, Comment).join(Post, User.id == Post.user_id).join(Comment, Comment.post_id == Post.id)
    TableOfContent = db.session.query(Family, FamilyFollowing, User, Content, ContentPhotos).\
        join(FamilyFollowing, Family.id == FamilyFollowing.FollowingFamilyId).\
        join(User, User.FamilyID == FamilyFollowing.FollowedFamilyId).\
        join(Content, User.id == Content.userId).\
        join(ContentPhotos, Content.id == ContentPhotos.contentId).all()
    
    DispContent = Content.query.filter(Content.userId == user_id).first()
    ContentPhoto = ContentPhotos.query.filter(ContentPhotos.contentId == DispContent.id).all()
    print(TableOfContent[0])
    posts = [row for row in TableOfContent if row[0].id == family_id]
    print(posts)

    return render_template('homefeed.html', Posts=posts)
    #User=user, Disp=DispContent, 

#post it to the backend




