from flask import Flask 
import threading
#from .read_data import read

from .events import socketio
from .routes import main 

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    app.register_blueprint(main)

    socketio.init_app(app)

    ''' data_thread = threading.Thread(target=read)
    data_thread.start() '''

    return app