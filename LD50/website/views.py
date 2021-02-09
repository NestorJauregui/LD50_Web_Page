from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/nosotros')
def nosotros():
    return render_template("nosotros.html")

@views.route('/nuestro-trabajo')
def nuestro_trabajo():
    return render_template("nuestro_trabajo.html")

@views.route('/nuestro-equipo')
def nuestro_equipo():
    return render_template("nuestro_equipo.html")

@views.route('/letal-shit')
def letal_shit():
    return render_template("letal_shit.html")

@views.route('/beats')
def beats():
    return render_template("beats.html")

@views.route('/blog')
def blog():
    return render_template("blog.html")

@views.route('/contacto')
def contacto():
    return render_template("contacto.html")