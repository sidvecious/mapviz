from flask import Flask, render_template, url_for, redirect, request
import csv

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=["GET", "POST"])
    def index():

        if request.method == 'GET':
            return render_template('index.html')

        #elif request.method == 'POST':
        #    coords = request.args.get('coords')
        #    #coords = 123
        #    return redirect(url_for("return_query", variable=coords))
        #else:
        #    "ooops, something goes wrong!"

    @app.route('/query/123', methods=["GET", "POST"])
    def return_query():
        if request.method == 'GET':
            filename = "templates/mocked_response.csv"
            with open(filename, 'r') as data:
                for line in csv.DictReader(data):
                    return line

        if request.method == 'POST':
            return "this is post method"

        else:
            return "ooops, something goes wrong!"


    return app

