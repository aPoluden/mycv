from flask import render_template
from mycv.application import app

@app.route('/')
def entry_point():
    return render_template('cv.html')