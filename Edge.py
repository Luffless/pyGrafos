class Edge:
    # Receive two Vertices and a integer
    def __init__(self, origin, destination, cost):
        self.origin = origin
        self.destination = destination
        self.cost = cost
    
    # Return a Vertice
    def getOrigin(self):
        return self.origin
      
    # Return a Vertice
    def getDestination(self):
        return self.destination
    
    # Return an integer
    def getCost(self):
        return self.cost