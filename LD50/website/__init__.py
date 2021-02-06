from flask import Flask

def crear_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Mucho pirobo si se pilla esta clave'

    return app