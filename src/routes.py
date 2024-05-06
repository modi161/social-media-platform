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

@app.route('/feedpage/<username>', methods=['GET', 'POST'])
# show the posts
def feedPage(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    family_id = user.FamilyID

    if request.method == 'POST':
        additional_data = request.form['additional_data']
        newFollowing = FamilyFollowing(FollowingFamilyId = family_id, FollowedFamilyId =  additional_data)
        db.session.add(newFollowing)
        db.session.commit()
    
    # show families to be followed
    alredy_followed = FamilyFollowing.query.filter(FamilyFollowing.FollowingFamilyId == family_id).all()
    alredy_followed_families = []
    for family in alredy_followed:
        alredy_followed_families.append(family.FollowedFamilyId)

    print(alredy_followed_families)
    
    print(alredy_followed)
    families = Family.query.filter(Family.id != family_id).all()

    TableOfContent = db.session.query(Family, FamilyFollowing, User, Content, ContentPhotos).\
        join(FamilyFollowing, Family.id == FamilyFollowing.FollowingFamilyId).\
        join(User, User.FamilyID == FamilyFollowing.FollowedFamilyId).\
        join(Content, User.id == Content.userId).\
        join(ContentPhotos, Content.id == ContentPhotos.contentId).all()
    
    families_filtered = [row for row in families if row.id not in alredy_followed_families]
    
    posts = [row for row in TableOfContent if row[0].id == family_id]
    

    return render_template('homefeed.html', User = user, Posts=posts, Families = families_filtered)
    #User=user, Disp=DispContent, 

#post it to the backend




