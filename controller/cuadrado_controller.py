from app import app
from flask import render_template
from model.cuadrado_model import *

@app.route('/cuadrado')
def cuadrado():
    return render_template('figura_view.html')