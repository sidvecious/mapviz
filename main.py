from flask import Flask, render_template, url_for

def create_app():
    app = Flask(__name__)

    @app.route('/static/<path:filename>', methods=["GET"])
    def index():
        return url_for('static', filename='index.html')

    return app

