
from flask import render_template , redirect ,request , flash,url_for, jsonify , session


from src import app,db
import sqlalchemy as sa
import time
from sqlalchemy import desc

from src.forms import Editform , Loginform , Signupform, ContentForm, DeleteContentForm
from src.models import User
from src.models import Content, ContentPhotos, Family, FamilyFollowing, UserLikedContent

from flask_login import current_user,login_user,login_required,logout_user
import os



@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()

    sform = Signupform()
    if current_user.is_authenticated:
        return redirect(url_for('feedPage', username=current_user.username))
    
    if sform.validate_on_submit() and sform.submit_signup.data:
        print("i entered the sign up")
        toggle = sform.toggle.data
        if toggle:
            user1 = User(username = sform.username.data,
                        email = sform.email.data,
                        FirstName=sform.firstname.data,
                        lastname=sform.lastname.data,
                        Gender=bool(sform.gender.data),
                        Birthdate=sform.birthdate.data,
                        FamilyID=sform.family_id.data,
                        FamilyRole=0,
                        bio="edit your bio",
                        photo="https://www.pngall.com/wp-content/uploads/12/Avatar-No-Background.png")
            user1.set_password(sform.password.data)
            db.session.add(user1)
            db.session.commit()
            login_user(user1)
            print(current_user.is_authenticated)
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('feedPage' , username =current_user.username))
        
    
    if form.validate_on_submit() and form.log.data:
        user = User.query.filter_by(email=form.email.data).first() # get the user first by email
        if user and user.check_password(form.password.data): # then check password ture or if the user not none
            login_user(user , remember=True)
            print(current_user.username)
            return redirect(url_for('feedPage', username=current_user.username))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    return render_template('index.html', form=form , sform = sform)

@app.route('/logout')
def logout():
    logout_user() 
    return redirect(url_for('login'))



@app.route('/user/<username>')
@login_required
def user(username):
    if current_user.username != username and not request.referrer:
        print()
        return redirect(url_for('logout'))
    user = db.first_or_404(sa.select(User).where(User.username == username)) #will trigger a 404 error if user not found in the db
    user_family = Family.query.filter_by(id = user.FamilyID).first()
    #print(user_family.familyname)
    return render_template('profile.html' , user = user , user_family = user_family , current_user = current_user)

@app.route('/feedpage/<username>', methods=['GET', 'POST'])
@login_required
# show the posts
def feedPage(username):
    if current_user.username != username:
        return redirect(url_for('logout'))
    user = db.first_or_404(sa.select(User).where(User.username == username))
    family_id = user.FamilyID
    
    form  = ContentForm()
    #When submit form, it will create object from Content including the submitted data.
    if form.validate_on_submit():
        content = Content(description = form.description.data, visibility = form.visibility.data, userId = form.userID.data, Type = form.type.data)
        
        db.session.add(content)
        db.session.commit()
        
        contentID = Content.query.order_by(desc(Content.timestamp)).first().id
        
        contentPhotos = ContentPhotos(contentId = contentID) #How to get above content id?
        print("Content ID:")
        print(contentID)
        
        if content.Type == 1:
            image = form.postImage.data
            print(image)
            if image:
                filename = f"{contentID}-{image.filename}"
                image_path = os.path.join("src/static/images", filename) #there is bug here, in multiple images case. User can not upload duplicate images in the same content 
                image.save(image_path)
                
                
                image_path = f"../static/images/{filename}"
                contentPhotos.photoUrl = image_path 
                
                print(image_path)
                
                
        else:
            image = form.albumImage.data
            if image:
                filename = f"{contentID}-{image.filename}"
                image_path = os.path.join("src/static/images", filename) #there is bug here, in multiple images case. User can not upload duplicate images in the same content 
                image.save(image_path)
                
                image_path = f"../static/images/{filename}"
                contentPhotos.photoUrl = image_path 
                
                print(image_path)
                
        db.session.add(contentPhotos)
        db.session.commit()



        

        #Clear everything (TO DO)
        form.description.data = None #to clear the form after adding post
        form.type.data = None
        form.visibility.data = None
        form.postImage.data = None
        

        
        #flash message
        
        #return same page, SHOULD I RETURN IT? or when click on add it will call this function and by default it will return to the page at the end
    
        
        
    
        
        
    
    
    
    
    
    

    #Like and Unlike part: (RASHAAAAAD Go and eat Fatosh!!!!!)
    # if request.method == 'POST':
    #     post_id = request.form.get('like') or request.form.get('unlike')
    #     action = 'like' if request.form.get('like') else 'unlike'
    #     if 'follow' in request.form:
    #         additional_data = request.form['additional_data']
    #         newFollowing = FamilyFollowing(FollowingFamilyId = family_id, FollowedFamilyId =  additional_data)
    #         db.session.add(newFollowing)
    #         db.session.commit()
    #     elif action == 'like':
    #         print("IM HERE")
    #         time.sleep(1)
    #         contentID = request.form['like']
    #         newLike = UserLikedContent(UserId = user.id, ContentId = post_id)
    #         db.session.add(newLike)
    #         db.session.commit()
    #     elif action == 'unlike':
    #         print("IM THERE")
    #         time.sleep(1)
    #         contentID = request.form['unlike']
    #         entry_to_delete = db.session.query(UserLikedContent).filter(UserLikedContent.ContentId == post_id, UserLikedContent.UserId == user.id).first()
    #         db.session.delete(entry_to_delete)
    #         db.session.commit()


        # show families to be followed
    alredy_followed = FamilyFollowing.query.filter(FamilyFollowing.FollowingFamilyId == family_id).all()
    alredy_followed_families = []
    for family in alredy_followed:
        alredy_followed_families.append(family.FollowedFamilyId)


    families = Family.query.filter(Family.id != family_id).all()

    TableOfContent = db.session.query(Family, FamilyFollowing, User, Content, ContentPhotos).\
        join(FamilyFollowing, Family.id == FamilyFollowing.FollowingFamilyId).\
        join(User, User.FamilyID == FamilyFollowing.FollowedFamilyId).\
        join(Content, User.id == Content.userId).\
        join(ContentPhotos, Content.id == ContentPhotos.contentId).all()
    
    families_filtered = [row for row in families if row.id not in alredy_followed_families]
    
    print(families_filtered)

    posts = [row for row in TableOfContent if row[0].id == family_id]
    # print(posts)


    # Liked content

    LikedContent = UserLikedContent.query.filter(UserLikedContent.UserId == user.id).all()
    alredy_liked = []
    for liked in LikedContent:
        alredy_liked.append(liked.ContentId)
    print(alredy_liked)
    return render_template('homefeed.html', User = user, Posts=posts, Families = families_filtered, Liked = alredy_liked, form = form)

#User=user, Disp=DispContent, 

#post it to the backend



@app.route('/familypage/<int:family_id>', methods=['GET', 'POST'])
@login_required
def family_page(family_id):
    
    deleteForm  = DeleteContentForm()
    
    if deleteForm.validate_on_submit():        
        contentId = deleteForm.contentID.data
        content = Content.query.get(contentId)

        
        photos = ContentPhotos.query.filter_by(contentId=contentId).all()
        
        #Delete row from the database, first photos then content
        for photo in photos:
            db.session.delete(photo)
            db.session.commit()

        db.session.delete(content)
        db.session.commit()
    
    
    if current_user.FamilyID != family_id and not request.referrer:
        return redirect(url_for('logout'))
    user_family = Family.query.filter_by(id = family_id).first()
    form = Editform()
    
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

    return render_template('family_page.html' ,current_user = current_user,form = form,followed_families = followed_families,user_family = user_family ,posts = posts , family_members = family_members, deleteForm = deleteForm)

    
    
