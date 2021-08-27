from flask import Flask, render_template, send_from_directory, request
from jinja2 import Markup

import src.database
from src.ui import formElement


app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets/css', path)

@app.route('/')
def home():
    page = {"title":"Test",
        "header":"Test",
        "content":"content"}
    return render_template('index.html',page=page)

@app.route('/form')
def form():
    page = {"title":"Test",
        "header":"Form Page",
        "content":Markup(formElement())}
    return render_template('index.html',page=page)


@app.route('/formsubmit', methods=["POST"])
def formSubmit():
    page = {"title":"Test",
        "header":"Form Results",
        "content":str(request.form['name'])}
    return render_template('index.html',page=page)
