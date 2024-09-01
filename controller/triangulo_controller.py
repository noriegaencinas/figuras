from app import app
from flask import render_template
from model.triangulo_model import *

@app.route('/circulo')
def triangulo():
    return render_template('figura_view.html')