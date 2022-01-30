from typing import List, TypedDict


class Card(TypedDict):
    suit: int
    value: int


class Play(TypedDict):
    combo: int
    comboValue: Card
    cards: List[Card]


class BoardPlay(TypedDict):
    playerIndex: int
    play: Play


class ClientGame(TypedDict):
    turn: int
    playerIndex: int
    winnerIndex: int
    currentPlayerIndex: int
    board: List[BoardPlay]
    cards: List[Card]
    remainingCardCount: List[int]


class ClientUser(TypedDict):
    socketId: str
    name: str


class DealOptions(TypedDict):
    playerCount: int
    randomHands: bool
    fourTwos: bool
    noFaces: bool
    distributeAll: bool


class LobbySettings(TypedDict):
    deal: DealOptions


class ClientLobby(TypedDict):
    id: str
    host: ClientUser
    players: List[ClientUser]
    spectators: List[ClientUser]
    settings: LobbySettings
    game: ClientGame
    roundNumber: int

class CallbackResult(TypedDict):
    result: int