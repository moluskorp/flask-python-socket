from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('message')
def handle_message(message):
    print("Received message: " + message)
    socketio.emit('message', message)

@socketio.on('disconnect')
def handle_disconnect():
    print("Client Disconnected")
    socketio.emit('message', 'Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True)