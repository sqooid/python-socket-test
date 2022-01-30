from typing import List
from socketio import Client

from interfaces import CallbackResult


def start_user(sio: Client, name: str = ''):
    sio.emit('createUser', name)


def start_lobby(sio: Client):
    def start_callback(response: CallbackResult):
        print('lobby start result:',response['result'])

    sio.emit('createLobby', callback=start_callback)


def join_lobby(sio: Client, lobby_id: str):
    def join_callback(response: CallbackResult):
        print('lobby join result:',response['result'])

    sio.emit('joinLobby', lobby_id, join_callback)


def start_game(sio: Client):
    sio.emit('startGame')


def send_play(sio: Client, card_indices: List[int] = None):
    sio.emit('makePlay', card_indices)
