from flask import Flask, render_template, redirect, url_for, request, abort

app = Flask(__name__)


@app.route('/')
def inicio():
    app.logger.debug('Empezando con Flask')
    app.logger.error('Empezando con Flask')
    return "Hola mundo Flask"


@app.route("/saludar/<nombre>", methods=['GET', 'POST', 'DELETE'])
def saludar(nombre):
    if request.method == 'POST':
        app.logger.debug('invocado con metodo POST')
    else:
        app.logger.debug('invocado con metodo GET')
    return f'Hola {nombre}'


@app.route("/mostrar/<int:edad>")
def mostrar(edad):
    edad += 1
    app.logger.debug(f'Edad{edad}')
    return render_template("mostrar.html", edad=edad)


@app.route("/redireccionar")
def redireccionar():
    return redirect(url_for('inicio'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html', error=error)


@app.route("/salir")
def salir():
    return abort(406)


if __name__ == "__main__":
    app.run(debug=True)
