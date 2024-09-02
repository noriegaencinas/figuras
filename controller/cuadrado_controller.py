from main import app
from flask import render_template
from model.cuadrado_model import *

@app.route('/cuadrado')
def cuadrado():
    return render_template('cuadrado_view.html')