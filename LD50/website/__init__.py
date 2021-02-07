from flask import Flask

def crear_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Mucho pirobo si se pilla esta clave'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app