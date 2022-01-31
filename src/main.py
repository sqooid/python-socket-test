import socketio
import handlers
import emits

if __name__ == '__main__':
    socket = socketio.Client()

    handlers.handle_socket_events(socket)

    socket.connect('https://sqooid.ddns.net')

    emits.start_user(socket)
    emits.start_lobby(socket)
    emits.start_game(socket)
