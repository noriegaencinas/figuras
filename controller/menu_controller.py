from main import app
from flask import render_template
from model.menu_model import *

@app.route('/')
@app.route('/menu')
@app.route('/index')
def menu_view():
    figuras = get_figuras()
    return render_template('menu_view.html', lista_figuras=figuras)

