from main import app
from flask import render_template, request
from model.cuadrado_model import *

@app.route('/cuadrado')
def cuadrado():
    return render_template('cuadrado_view.html')

@app.route('/cuadrado/calcular', methods=['POST'])
def cuadrado_calcular():
    accion = request.form['accion']
    lado = float(request.form['lado'])
    cuadrado = Cuadrado(lado)

    if accion == 'calcular_area':
        resultado = cuadrado.calcular_area()
    elif accion == 'calcular_perimetro':
        resultado = cuadrado.calcular_perimetro()
        
    return render_template('cuadrado_view.html', resultado=[accion, resultado])   