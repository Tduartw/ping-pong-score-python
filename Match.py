import random

class Match:

    def __init__(self, name):
        self.name = name
        self.serve = False
        self.score = 0
        self.serve_total = 0
        self.opponent = None
        self.win = False

    def playWith(self, other):
        self.serve = True
        self.opponent = other

        while not self.win and not self.opponent.win:

            self.serve_total += 1

            self.changeSetsEvery(5)
            #Salvar o perdedor do set para fazer a comparação de 20:20 
            winner = random.choice([self, self.opponent])

            self.addScoreTo(winner)




    def changeSetsEvery(self, sets):
        if  self.serve_total == sets :
                self.serve_total = 0
                self.toggleTurn()


    def toggleTurn(self):
        if self.serve == True:
            self.opponent.serve = True
            self.serve = False
            print(f'Saque do jogador: {self.opponent.name}')
        else:
            self.serve = True
            self.opponent.serve = False
            print(f'Saque do jogador: {self.name}')
    

    
    def addScoreTo(self, winner):
        winner.score += 1
        print(f"Ponto para: {winner.name}")
        print(f'({self.score} : {self.opponent.score})')
        self.checkWinner()


    def checkWinner(self):

        #TODO adicionar na condição se o oponente tem 2 pontos a menos que player
        #if winner.score == 21 and self.loser < winner.score - 2
            #print(f"Fim de jogo, {player.name} ganhou")
            #player.win = True
        pass

player_a = Match('Jogador A')
player_b = Match('Jogador B')


player_a.playWith(player_b)
