import json
from interfaces import ClientLobby


def handle_socket_events(sio):
    @sio.on('syncLobby')
    def on_sync_lobby(lobby: ClientLobby):
        print(json.dumps(lobby,indent=2))
