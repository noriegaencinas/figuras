from main import app
from flask import render_template
#from model.menu_model import *

@app.route('/')
def menu_view():
    return render_template('menu_view.html')

