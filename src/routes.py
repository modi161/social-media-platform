from flask import render_template , redirect ,request # type: ignore

from src import app

@app.route('/')
def start_page():
    return render_template('index.html')








