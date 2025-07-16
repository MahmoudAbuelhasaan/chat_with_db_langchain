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
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    from app.chat import bp as chat_bp
    app.register_blueprint(chat_bp)
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp)
    from app.commands.seeds import seed_db
    app.cli.add_command(seed_db)


    return app
    

# flask login user loader
@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))
