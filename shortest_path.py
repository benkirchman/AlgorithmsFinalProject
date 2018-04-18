
def getShortestPath(edges, vertices):
    distances = [float("inf") for vertex in vertices]
    predeccesors = [None for vertex in vertices]
    distances[0] = 0
    for vertex in vertices:
        for edge in edges:
            #print("edge: " + edge.asString())
            #print("distances: " + str(distances))
            #print("predeccesors: " + str(predeccesors))
            if(distances[edge.endIndex] > distances[edge.startIndex] + edge.weight):
                #print("true")
                distances[int(edge.endIndex)] = float(distances[edge.startIndex] + edge.weight)
                predeccesors[int(edge.endIndex)] = edge
    for edge in edges:
        if distances[edge.endIndex] > distances[edge.startIndex] + edge.weight:
            print("Error negative cycle")
    '''
    node = vertices[-1]
    shortest_path = []
    while(node > 0):
        shortest_path.append(predeccesors[node])
        node = predeccesors[node].startIndex
    '''
    return distances


class Edge:
    def __init__(self, startIndex, endIndex, weight):
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.weight = weight
    def asString(self):
        return "(" + str(self.startIndex) + "," + str(self.endIndex) + ", w: " + str(self.weight) +") "
