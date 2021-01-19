from flask import Flask, render_template

from frontend.app.seller import seller

app = Flask(__name__)
app.register_blueprint(seller)

name = 'olist'
menu = [
    {'name': 'Sellers',
     'route': '/sellers'},
]


@app.route('/')
def index():
    return render_template('index.html', name=name, list=menu)
