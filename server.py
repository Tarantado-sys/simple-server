from flask import Flask, request, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.before_request
def log_request():
    traffic_data = {
        'method': request.method,
        'path': request.path,
        'remote_addr': request.remote_addr,
        'user_agent': request.headers.get('User-Agent', 'Unknown'),
        'headers': dict(request.headers),
        'timestamp': str(request.environ.get('REQUEST_TIME', 'Unknown'))
    }
    socketio.emit('traffic', traffic_data, namespace='/dashboard')

@app.route("/")
def home():
    return send_from_directory('html', 'index.html')
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8080)