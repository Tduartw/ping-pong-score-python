class Match:

    def __init__(self):
        self.set = 1
        self.server_is = ''

    def addPointTo(self, player):
        new_score = 1
        new_score += player.points 
        
        player.setScore(new_score)
  

    def addServeTo(self, player):
        new_serve = 1
        new_serve += player.serve 
        
        player.setServe(new_serve)


    def checkServeTurn(self, player_a, player_b):
        self.server_is = player_a.name
        
        if player_a.getServe() == 5:
            player_a.setServe(0)
            self.server_is = player_b.name
        else:
            player_b.setServe(0)
            self.server_is = player_a.name
       