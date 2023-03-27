from flask import Flask, redirect,url_for,render_template,send_file

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config') #where to find config file


