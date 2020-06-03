from flask import Flask, render_template, Response, request, redirect, url_for
from db import Check, Save, Send
app = Flask(__name__)
@app.route('/')
def main():
  return render_template('index.html', data=Check())
@app.route('/about', methods=['GET', 'POST'])
def about():
  return render_template('about.html')
@app.route('/send', methods=['GET', 'POST'])
def send():
  contactData = request.form['contact']
  Send(contactData)
  return render_template('redirect.html')
@app.route('/contact')
def contact():
  return render_template('contact.html')
@app.route('/clicked', methods=['GET', 'POST']) 
def clicked():
    e = Check()
    print(e)
    o = e + 1
    print(o)
    Save(o, e)
    return render_template('index.html', data=o)
app.run(host='0.0.0.0', port=8080)