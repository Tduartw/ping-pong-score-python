class Match:

    def __init__(self):
        self.set = 1

    def addPointTo(self, player):
        new_score = 1
        new_score += player.points 
        
        player.setScore(new_score)


    def addServeTo(self, player):
        new_serve = 1
        new_serve += player.serve 
        
        player.setServe(new_serve)

   
