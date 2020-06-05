#This code is by Noel. Sorry about the bad comments, they are for a friend
from flask import Flask, render_template, Response, request, redirect, url_for
from db import Check, Save, Send
app = Flask(__name__)
#This runs when you go to /
@app.route('/')
def main():
  #Renders index.html, and checks what the current data us and sends it.
  return render_template('index.html', data=Check())
#This would run at /about
@app.route('/about', methods=['GET', 'POST'])
def about():
  #Renders about.html
  return render_template('about.html')
#This is NOT the contact form page, this is what happends when you SUBMIT it.
@app.route('/send', methods=['GET', 'POST'])
def send():
  #This gets what you put in the contact form
  contactData = request.form['contact']
  #Then, it calls the Send function in DB.py with the data
  Send(contactData)
  #Then it renders redirct.html, which, self explanitory, redircts you!
  return render_template('redirect.html')
#THIS is the contact form, running at /contact
@app.route('/contact')
def contact():
  #This renders contact.html
  return render_template('contact.html')
#this is what happends when you click the click me button, because it redircts you to the /clicked page
@app.route('/clicked', methods=['GET', 'POST']) 
def clicked():
    #From here on is not very good code sry
    #First it gets the current number, which is needed using the Check() functuon from DB.py
    before = Check()
    print(e)
    #Then it adds one to create the after
    after = before + 1
    print(after)
    #Then it calks the save function in DB.py
    Save(after, before)
    #Then it renders index.html again
    return render_template('index.html', data=o)
#This will run the site
app.run(host='0.0.0.0', port=8080)