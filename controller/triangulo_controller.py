from main import app
from flask import render_template, request
from model.triangulo_model import *

@app.route('/triangulo')
def triangulo():
    return render_template('triangulo_view.html')

@app.route('/triangulo/calcular', methods=['POST'])
def triangulo_calcular():
    accion = request.form['accion']
    base = float(request.form['base'])
    altura = float(request.form['altura'])
    triangulo = Triangulo(base, altura)

    if accion == 'calcular_area':
        resultado = triangulo.calcular_area()
    elif accion == 'calcular_perimetro':
        resultado = triangulo.calcular_perimetro()    
    return render_template('triangulo_view.html', resultado=[accion, resultado])