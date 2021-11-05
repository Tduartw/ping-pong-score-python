class Match:

    def __init__(self):
        self.sets = 0
        self.server_is = ''


    def setTotalSets(self, interator):
        self.sets = interator

    def getTotalSets(self):
        return self.sets
        
    def addScoreTo(self, player):
        new_score = 1
        new_score += player.getScore() 
        
        player.setScore(new_score)

    def addGoldenScoreTo(self, player):
        new_golden_score = 1
        new_golden_score += player.getGoldenScore() 
        
        player.setGoldenScore(new_golden_score)



    def toggleTurn(self, player_a, player_b):
        if player_a.getServe() == True:
            player_b.setServe(True)
            self.server_is = player_b.getName()
            player_a.setServe(False)
        else:
            player_a.setServe(True)
            self.server_is = player_a.getName()
            player_b.setServe(False)
    
 