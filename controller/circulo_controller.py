from main import app
from flask import render_template, request
from model.circulo_model import *

@app.route('/circulo')
def circulo():
    return render_template('circulo_view.html')

@app.route('/circulo/calcular', methods=['POST'])
def circulo_calcular():
    accion = request.form['accion']
    radio = float(request.form['radio'])
    circulo = Circulo(radio)
    nombre_accion = "área" if accion == 'calcular_area' else "perímetro"

    if accion == 'calcular_area':        
        resultado = circulo.calcular_area()        
    elif accion == 'calcular_perimetro':        
        resultado = circulo.calcular_perimetro()   

    return render_template('circulo_view.html', resultado=[nombre_accion, resultado])    
        













#En el diagrama dice double, pero en python no hay double, se usa float