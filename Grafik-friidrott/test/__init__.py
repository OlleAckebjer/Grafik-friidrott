from flask import Flask 
from .extensions import sse
import threading
#from .read_data import read

from .events import socketio
from .routes import main 

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    app.config["REDIS_URL"] = "redis://localhost:5000"  # Configure Redis for Flask-SSE
    app.register_blueprint(sse, url_prefix="/stream")  # Register the SSE blueprint

    app.register_blueprint(main)

    socketio.init_app(app)

    return app