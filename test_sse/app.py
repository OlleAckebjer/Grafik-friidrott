from flask import Flask, render_template
from flask_sse import sse
import time
import os

app = Flask(__name__)
app.config['REDIS_URL'] = os.environ.get('REDIS_URL', 'redis://localhost:5000')
app.register_blueprint(sse, url_prefix='/stream')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_data')
def send_data():
    data = 'Hello from the server!'
    sse.publish(data, type='data_event')
    return 'Data sent'

if __name__ == '__main__':
    app.run()
