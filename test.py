import shortest_path as sp
import generator as gen
def basicTest():
    edges = [sp.Edge(0,1,1),sp.Edge(1,2,2),sp.Edge(0,2,2), sp.Edge(1,3,1), sp.Edge(2,3,2)]
    vertices = range(4)
    for edge in  edges :
        print(edge.asString())
    distances = sp.getShortestPath(edges, vertices)
    print(distances)

def directTest():
    edges = [sp.Edge(0,1,1),sp.Edge(1,2,2),sp.Edge(0,2,2), sp.Edge(1,3,1), sp.Edge(2,3,2), sp.Edge(0,3,8)]
    vertices = range(4)
    for edge in  edges :
        print(edge.asString())
    distances = sp.getShortestPath(edges, vertices)
    print(distances)
def negativeTest():
    edges = [sp.Edge(0,1,1),sp.Edge(1,2,-2),sp.Edge(0,2,2), sp.Edge(1,3,1), sp.Edge(2,3,2)]
    vertices = range(4)
    for edge in  edges :
        print(edge.asString())
    distances = sp.getShortestPath(edges, vertices)
    print(distances)
def testCycle():
    n = 50
    distances = sp.getShortestPath(gen.generateCycle(n), range(n))
    print(distances)
def testIncomplete():
    n = 50
    distances = sp.getShortestPath(gen.generateIncompleteGraphRandomWeights(n), range(n))
    print(distances)
basicTest()
directTest()
negativeTest()
testCycle()
testIncomplete()
