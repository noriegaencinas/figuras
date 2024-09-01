from app import app
from flask import render_template
from model.circulo_model import *

@app.route('/circulo')
def circulo():
    return render_template('figura_view.html')

# @app.route('/circulo/area')
# def circulo_area():
#     radio = float(request.args.get('radio'))
#     circulo = Circulo(radio)
#     return render_template('circulo_area.html', circulo=circulo)
# 
# @app.route('/circulo/perimetro')
# def circulo_perimetro():
#     radio = float(request.args.get('radio'))
#     circulo = Circulo(radio)
#     return render_template('circulo_perimetro.html', circulo=circulo)


#En el diagrama dice double, pero en python no hay double, se usa float