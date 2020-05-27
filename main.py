from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def redirct():
  return render_template('index.html')
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")
app.run(host='0.0.0.0', port=8080)