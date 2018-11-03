
import flask
from flask import request, jsonify
from flask_socketio import SocketIO, send, emit

app = flask.Flask(__name__)
app.config["DEBUG"] = True
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)


@socketio.on('DRAG_STARTED')
def handle_drag_started(payload):
    emit('drag_started_update', payload, broadcast=True, include_self=False)


@socketio.on('DRAGGING')
def handle_dragging(payload):
    emit('dragging_update', payload, broadcast=True, include_self=False)


@socketio.on('DRAG_STOPPED')
def handle_drag_stopped(payload):
    emit('drag_stopped_update', payload, broadcast=True, include_self=False)


@socketio.on('DRAG_COMMITED')
def handle_drag_commited(payload):
    emit('drag_commited_update', payload, broadcast=True, include_self=False)


@socketio.on('DRAG_DISCARDED')
def handle_drag_discarded(payload):
    emit('drag_discarded_update', payload, broadcast=True, include_self=False)


@socketio.on('ADD_LINK')
def handle_add_link(payload):
    emit('add_link_update', payload, broadcast=True, include_self=False)


@app.route('/', methods=['GET'])
def home():
    return "hello"
