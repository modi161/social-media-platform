from flask import render_template , redirect ,request , flash,url_for

from src import app,db
import sqlalchemy as sa


from src.forms import editform
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



@app.route('/familypage/<int:family_id>', methods=['GET', 'POST'])
def family_page(family_id):
    user_family = Family.query.filter_by(id = family_id).first()
    form = editform()
    
    if form.validate_on_submit():
        if form.bio.data:
            user_family.bio = form.bio.data
            db.session.commit()  # Commit changes to the database
            return redirect(url_for('family_page', family_id=family_id))
        else:
            # Handle form validation failure if needed
            pass
    else:
        # This block only executes when the page first loads or if validation fails
        if user_family:
            form.bio.data = user_family.bio
    
        
    posts = db.session.query(User,  Content, ContentPhotos)\
    .join(Family, User.FamilyID == Family.id)\
    .join(Content, User.id == Content.userId)\
    .join(ContentPhotos, ContentPhotos.contentId == Content.id)\
    .filter(Family.id == user_family.id)\
    .order_by(Content.timestamp.desc())\
    .all()
    
    
    family_members = db.session.query(User).join(Family,User.FamilyID == Family.id)\
    .filter(Family.id == user_family.id)\
    .all()
    
    family_following = db.session.query(FamilyFollowing.FollowedFamilyId)\
    .join(Family,Family.id == FamilyFollowing.FollowingFamilyId)\
    .filter(Family.id == user_family.id)\
    .all()
    family_followed_ids = [id[0] for id in family_following]
    
    followed_families = db.session.query(Family).filter(Family.id.in_(family_followed_ids)).all()   

    return render_template('family_page.html' ,form = form,followed_families = followed_families,user_family = user_family ,posts = posts , family_members = family_members)

    

@app.route('/familypage/DeletePost/<int:content_id>')
def family_page_delete_content(content_id):
    
    photos = ContentPhotos.query.filter_by(contentId=content_id).all()
    content = Content.query.get(content_id)
    user_id = getattr(content, "userId")
    
    user = User.query.get(user_id)
    family_id = getattr(user, "FamilyID")
    
    #Delete row from the database, first photos then content
    for photo in photos:
        db.session.delete(photo)
        db.session.commit()

        
        
    db.session.delete(content)
    db.session.commit()
        
    return family_page(family_id)
    
    
