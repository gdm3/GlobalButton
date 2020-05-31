from flask import Flask, render_template, Response, request, redirect, url_for
from db import Check, Save
print(Check())
app = Flask(__name__)
data = Check()
@app.route('/')
def main():
  return render_template('index.html', data=data)
@app.route('/clicked', methods=['GET', 'POST']) 
def clicked():
    e = Check()
    print(e)
    o = e + 1
    print(o)
    Save(o, e)
    print("Saving one")
    
    return render_template('index.html', data=o)
app.run(host='0.0.0.0', port=8080)