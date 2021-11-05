class Player:
    def __init__(self, name):
        self.name = name
        self.serve = False
        self.score = 0
        self.golden_score = 0
    
    
    def getName(self):
        return self.name

    def setGoldenScore(self, golden_score):
        self.golden_score = golden_score

    def getGoldenScore(self):
        return self.golden_score

    def setScore(self, new_score):
        self.score = new_score

    def getScore(self):
        return self.score


    def setServe(self, serve_state):
        self.serve = serve_state

    def getServe(self):
        return self.serve

