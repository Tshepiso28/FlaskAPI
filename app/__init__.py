from flask import Flask
from app.routes.user_route import user_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_blueprint, url_prefix='/users')
    return app
