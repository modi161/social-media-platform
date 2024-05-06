from flask import render_template , redirect ,request , flash

from src import app,db
import sqlalchemy as sa
from src.models import User

@app.route('/')
def start_page():
    return render_template('index.html')

@app.route('/user/<username>')
# login_required should be added here ////////////////////
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username)) #will trigger a 404 error if user not found in the db
    return render_template('profile.html' , user = user)

#post it to the backend




