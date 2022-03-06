#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators
from flask_mail import Mail, Message
import os

DEVELOPMENT_ENV  = True

mail = Mail()

app = Flask(__name__)


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

app_data = {
    "name":         "YMCA",
    "description":  "A basic Flask app",
    "html_title":   "YMCA Research",
    "project_name": "YMCA Research",
}


class ContactForm(Form):
  name = StringField("Name",  [validators.DataRequired("Please enter your name.")])
  email = StringField("Email",  [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
  subject = StringField("Subject",  [validators.DataRequired("Please enter a subject.")])
  message = TextAreaField("Message",  [validators.DataRequired("Please enter a message.")])
  submit = SubmitField("Send")


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'stats141xpbdd@gmail.com'
app.config["MAIL_PASSWORD"] = 'BDD141141'
 
mail.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', app_data=app_data)


@app.route('/program')
def program():
    return render_template('program.html', app_data=app_data)

@app.route('/play')
def play():
    return render_template('PLAY.html', app_data=app_data)

@app.route('/yima')
def yima():
    return render_template('YIMA.html', app_data=app_data)

@app.route('/yng')
def yng():
    return render_template('Y&G.html', app_data=app_data)


@app.route('/service')
def service():
    return render_template('service.html', app_data=app_data)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form, app_data=app_data)
    else:
      msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
      msg.body = """
      From: %s &lt;%s&gt;
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return render_template('contact.html', success=True)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form, app_data=app_data)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response

if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)