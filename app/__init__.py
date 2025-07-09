from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_socketio import SocketIO
from config import Config
from flask_login import LoginManager
from flask_bcrypt import Bcrypt



db = SQLAlchemy()
socketio = SocketIO()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # intialize extinsions

    db.init_app(app)
    socketio.init_app(app,cors_allowed_origins='*')
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    bcrypt.init_app(app)


    return app
    


