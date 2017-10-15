from flask_socketio import SocketIO

from application.app import app, db

socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)
