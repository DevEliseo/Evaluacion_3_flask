from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
#ruta ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio=None
    estado=None

    if request.method == "POST":
        # se solicitan los datos al formulario
        nota1=float(request.form["nota1"])
        nota2=float(request.form["nota2"])
        nota3=float(request.form["nota3"])
        asistencia=float(request.form["asistencia"])

        promedio = round((nota1+nota2+nota3)/3)#promedio de las notas

        if promedio >=40 and asistencia >=75:# condicional para los resultados de aprobado o reprobado
            estado='APROBADO'
        else:
            estado='REPROBADO'

    return render_template("notas.html",promedio=promedio,estado=estado)

#ruta ejercicio 2

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mayor= None
    cantidad_caracteres= None

# solicitamos los datos del formulario
    if request.method == "POST":
        nombre1=request.form["nombre1"].strip()
        nombre2=request.form["nombre2"].strip()
        nombre3=request.form["nombre3"].strip()

        # creo lista con nombres para evaluarlos  rapidamente
        nombres=[nombre1,nombre2,nombre3]
        nombre_mayor=max(nombres, key=len)#de la lista nombres va a contar los caracteres de cada nombre
        cantidad_caracteres=len(nombre_mayor)# contar los caracteres de el nombre mayor

    return  render_template("nombres.html",
                            nombre_mayor=nombre_mayor,
                            cantidad_caracteres=cantidad_caracteres,)


if __name__ == '__main__':
    app.run(debug=True)