from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('prueba.html', title='Prueba Flask', 
                            heading='Bienvenidos a Flask!', 
                            items=['Item 1', 'Item 2', 'Item 3'])

if __name__ == "__main__":
    app.run(debug=True)
"""
@app.route('/')
#Cuando el usuario acceda a esta url, flask ejecutara la funcion home().

def home():
    return 'Hello, World!'
"""

"""
@app.route('/post', methods=['POST'])
#La ruta '/post' solo aceptara solicitudes POST

def post_method():
    return 'you sent a POST request'
"""

"""
@app.route('/user/<username>')
#Cuando alguien visita esta ruta, la funcion show_user_profile se llama con el username

def show_user_profile(username):
    return f'User {username}'
"""

"""
@app.route('/')
def home():
    return render_template('template.html', title='Home Page', heading='Welcome!', 
                            items=['Item 1', 'Item 2', 'Item 3'])
    #render_template funcion que toma el nombre de una plantilla y las variables que quieres pasar a ella.
"""

"""
# Instalar con pip install Flask
from flask import Flask, request, jsonify

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
import os, time
"""