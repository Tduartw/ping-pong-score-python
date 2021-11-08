import random
from time import sleep

class Match:

    def __init__(self, name):
        self.name = name
        self.serve = False
        self.score = 0
        self.serve_total = 0
        self.opponent = None
        self.loser = None
        self.win = False


    def playWith(self, other):
        self.serve = True
        self.opponent = other   
        

        while not self.win and not self.opponent.win:
    
            self.serve_total += 1

            self.checkSet()

            winner = self.selectSetWinner()
            self.addScoreTo(winner)

            sleep(.3)


    def checkSet(self):
        if self.score == 20 and self.opponent.score == 20:
            self.serve_total = 1
            self.changeSetsEvery(2)
        else:
            self.changeSetsEvery(5)


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
        self.checkWinner(winner)
        

    def checkWinner(self, winner):

        if winner.score >= 21 and self.loser.score <= winner.score  - 2:
            print(f"Fim de jogo, {winner.name} ganhou")
            winner.win = True
        
    

    def selectSetWinner(self):
        list = [self, self.opponent]
        random_number = random.randrange(2)
        
        winner = list[random_number]
        
        for i in range(len(list)):
            if  i != random_number:
                self.loser = list[i]

        return winner








player_a = Match('Jogador A')
player_b = Match('Jogador B')


player_a.playWith(player_b)
