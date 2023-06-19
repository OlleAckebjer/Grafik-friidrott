from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfhsdajkhfajh2312234hjsdhfjh32234'
socketio = SocketIO(app)

@app.route("/", methods=["POST", "GET"])
def main():
    return render_template("test.html")

@socketio.on('background_change')
def handle_background_change(data):
    color = data['color']
    # Perform background change logic here
    # Broadcast the background change to all connected clients
    socketio.emit('background_change', {'color': color}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5052, debug=True)

