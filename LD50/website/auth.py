from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/ingresar')
def ingresar():
    return "<h1>Ingresar</h1>"

@auth.route('/salir')
def salir():
    return "<h1>Salir</h1>"

@auth.route('/registrarse')
def registrarse():
    return "<h1>Registrarse</h1>"