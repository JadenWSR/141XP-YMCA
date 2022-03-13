#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template

DEVELOPMENT_ENV  = True

app = Flask(__name__)

app_data = {
    "name":         "YMCA",
    "description":  "A basic Flask app",
    "html_title":   "YMCA Research",
    "project_name": "STATS 141XP YMCA Research",
}


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


@app.route('/results')
def service():
    return render_template('Results.html', app_data=app_data)


@app.route('/contact')
def contact():
    return render_template('contact.html', app_data=app_data)

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