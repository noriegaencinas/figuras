def get_figuras():
    return [
        {
            'nombre': 'Círculo',
            'imagen': '/static/img/circle.svg',
            'url': 'circulo'
        },
        {
            'nombre': 'Cuadrado',
            'imagen': '/static/img/square.svg',
            'url': 'cuadrado'
        },
        {
            'nombre': 'Triángulo',
            'imagen': '/static/img/triangle.svg',
            'url': 'triangulo'
        }
    ]

testing = True
def test():
    print('Testing menu_model.py')
    figuras = get_figuras()
    print(figuras)    
    for figura in figuras:
        print(figura['nombre'])
        print(figura['imagen'])
        print(figura['url'])        
        print("---------------")    
if testing:
    test()