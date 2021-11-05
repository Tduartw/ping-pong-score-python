from match import Match 
from player import Player
import time
import random

player_a = Player("Jogador A")
player_b = Player("Jogador B")
match = Match()

is_playing = True
is_draw = False

players = [player_a, player_b]

match.toggleTurn(player_a, player_b)

counter = 0

print(" ..... Hora da partida ..... ")
while is_playing:

    counter += 1

    match_set = match.getTotalSets()
    match_set += 1
    match.setTotalSets(match_set)

    print(f'SET: {counter}')

    if player_a.getScore() == 20 and player_b.getScore() == 20:
        if match.getTotalSets() == 3:
            match.setTotalSets(1)
            match.toggleTurn(player_a, player_b)

        print(f'Vez de: {match.server_is}') 

        winner = random.choice(players)
        
        if player_a.getGoldenScore() == 1 and player_b.getGoldenScore() == 1:
            continue
        
        match.addGoldenScoreTo(winner)


        print(f"{player_a.getName()} ({ player_a.getGoldenScore()} : { player_b.getGoldenScore()}) {player_b.getName()}")

        for index, player in enumerate(players):
            if player.getGoldenScore() == 2:
                print(f'{player.getName()} ganhou')
                is_playing = False
        
    else:
        if match.getTotalSets() == 6:
            match.setTotalSets(1)
            match.toggleTurn(player_a, player_b)

        print(f'Vez de: {match.server_is}') 

        winner = random.choice(players)
        match.addScoreTo(winner)

        print(f"{player_a.getName()} ({ player_a.getScore()} : { player_b.getScore()}) {player_b.getName()}")

     
        for index, player in enumerate(players):
            if player.getScore() == 21:
                print(f'{player.getName()} ganhou')
                is_playing = False
        

    

        
    

    
    
