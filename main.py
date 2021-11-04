from match import Match 
from player import Player
import time
import random

player_a = Player("Jogador A")
player_b = Player("Jogador B")

match = Match()

is_playing = True


match.setServeTurn(player_a, player_b)



print(" ..... Hora da partida ..... ")

while is_playing:
    print(f'Vez de: {match.server_is}')
    time.sleep(1)
    scored = random.randrange(2)

    if scored == 0:
        match.addPointTo(player_a)
    else:
        match.addPointTo(player_b)

    match.checkServeTurn(player_a, player_b)
