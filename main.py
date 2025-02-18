
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "IDGS801"
    lista = ("juan", "pedro", "luis")
    return render_template('index.html', titulo=titulo, lista = lista)

@app.route('/ejemplo1')
def ejemplo1():
    return render_template('ejemplo1.html')

@app.route('/ejemplo2')
def ejemplo2():
    return render_template('ejemplo2.html')



@app.route('/hola')
def hola():
    return "<h1>Hola, Mundo!</h1>"

@app.route('/user/<string:user>')
def user(user):
    return f'<h1>Hola, {user}!</h1>'

@app.route('/numero/<int:n>')
def numero(n):
    return f'<h1>El número es: {n}</h1>'

@app.route('/user/<int:id>/<string:username>')
def user2(id, username):
    return f'<h1>El usuario es: {username} con id: {id}</h1>'

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return f'<h1>La suma es: {n1 + n2}</h1>'

@app.route('/default/')
@app.route('/default/<string:param>')
def func(param='juan'):
    return f'''
        <form action="/default/" method="get">
            <label for="param">Ingresa el parámetro:</label>
            <input type="text" id="param" name="param" value="{param}">
            <button type="submit">Enviar</button>
        </form>
        <h1>El parámetro es: {param}</h1>
    '''

@app.route('/operacion')
def operacion():
    return render_template('operasbas.html')

@app.route('/resultados', methods={'POST'})
def resultados():
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    return f'la suma de tu {n1} * {n2} es igual a: {int(n1) * int(n2)}'

@app.route('/operacion1')
def operacion1():
    return render_template('OperasBas1.html')

@app.route('/resultado1', methods=['POST'])
def resultado1():
    num1 = request.form.get('n1', type=float)
    num2 = request.form.get('n2', type=float)
    operacion = request.form.get('operacion')
    
    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
    elif operacion == 'division':
        resultado = num1 / num2 if num2 != 0 else 'Error: División por cero'
    elif operacion == 'potencia':
        resultado = num1 ** num2
    else:
        resultado = 'Operación no válida'
    
    return f'El resultado de la {operacion} es: {resultado}'

@app.route('/cinepolis')
def cinepolis():
    return render_template('cinepolis.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    nombre = request.form.get('nombre')
    compradores = int(request.form.get('compradores'))
    boletos = int(request.form.get('boletos'))
    tarjeta_cineco = request.form.get('tarjeta') == 'si'

    while True:
        if boletos < 1 or boletos > compradores * 7:
            print(f"Cada persona puede comprar hasta 7 boletos. En total pueden comprar hasta {compradores * 7}.")
            opcion = request.form.get('corregir')
            if opcion == "personas":
                compradores = int(request.form.get('nuevo_compradores'))
                boletos = int(request.form.get('boletos'))
            elif opcion == "boletos":
                boletos = int(request.form.get('nuevo_boletos'))
            else:
                return render_template('correccion.html')
        else:
            break 

    precio_unitario = 12.00
    total_bruto = boletos * precio_unitario

    if boletos > 5:
        descuento = 0.15
    elif 3 <= boletos <= 5:
        descuento = 0.10
    else:
        descuento = 0.0

    total_descuento = total_bruto * descuento
    total_a_pagar = total_bruto - total_descuento

    if tarjeta_cineco:
        total_a_pagar *= 0.90

    return render_template('resultado.html', nombre=nombre, compradores=compradores, boletos=boletos, total=round(total_a_pagar, 2))

@app.route('/zodiaco_chino')
def zodiaco_chino():
    return render_template('zodiaco_chino.html')

@app.route('/resultado_zodiaco', methods=['POST'])
def resultado_zodiaco():
    nombre = request.form.get('nombre')
    appellidoPaterno = request.form.get('appellidoPaterno')
    appellidoMaterno = request.form.get('appellidoMaterno')

    fecha_nacimiento = request.form.get('fecha_nacimiento')
    sexo = request.form.get('sexo')

    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')

    dia = fecha_nacimiento.day
    mes = fecha_nacimiento.month
    ano = fecha_nacimiento.year

    fecha_actual = datetime.now()
    edad = fecha_actual.year - ano
    if (fecha_actual.month, fecha_actual.day) < (mes, dia):
        edad -= 1

    signos_chinos = ["Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente", 
                     "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"]
    signo_chino = signos_chinos[(ano - 1900) % 12]

    imagen_signo = f"{signo_chino.lower()}.jpg"

    return render_template('resultado_zodiaco.html', nombre=nombre, appellidoPaterno=appellidoPaterno, appellidoMaterno=appellidoMaterno, edad=edad, 
                           signo_chino=signo_chino, imagen_signo=imagen_signo, sexo=sexo)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
