from flask import Flask, render_template, Response, request, redirect, url_for
from db import Check
app = Flask(__name__)
data = 3
@app.route('/')
def redirct():
  return render_template('index.html', data=data)
@app.route('/clicked', methods=['GET', 'POST']) 
def clicked():
    print ("Saving one")
    return ("nothing")
app.run(host='0.0.0.0', port=8080)