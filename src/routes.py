from flask import render_template , redirect ,request , flash

from src import app

@app.route('/')
def start_page():
    return render_template('index.html')

#post it to the backend 






