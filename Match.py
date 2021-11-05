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

        while not self.win:

            self.serve_total += 1

            self.changeSetsEvery(5)
     
            winner = random.choice([self, self.opponent])
            self.addScoreTo(winner)

            print(f'{self.score} : {self.opponent.score}')
        

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
    

    @classmethod
    def addScoreTo(winner):
        winner.score += 1
        print(f'{winner.name} marcou um ponto!')


player_a = Match('Jogador A')
player_b = Match('Jogador B')


player_a.playWith(player_b)
