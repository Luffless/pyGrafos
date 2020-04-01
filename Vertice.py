class Vertice:
    # Receive an integer
    def __init__(self, idetifier):
        self.idetifier = idetifier
        self.visited = False
        
    # Return an integer
    def getId(self):
        return self.idetifier
    
    def getVisited(self):
        return self.visited
        
    def setVisited(self, value):
        self.visited = value