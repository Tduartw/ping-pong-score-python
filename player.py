class Player:
    def __init__(self, name):
        self.name = name
        self.serve = 0
        self.points = 0


    def setScore(self, new_points):
        self.points = new_points

    def setServe(self, new_serve):
        self.serve = new_serve

    def getServe(self):
        return self.serve
