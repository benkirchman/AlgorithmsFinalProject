from random import shuffle
from shortest_path import Edge

def generateCompleteGraphRandomWeights(n):
    edges = []
    weightRange = [i for i in range(1,n+1)]
    shuffle(weightRange)
    count = 0
    for i in range(n):
        for j in range(n):
            edges.append(Edge(i,j,weightRange[count]))
            count+=1
            count = count % n
    return edges

def generateIncompleteGraphRandomWeights(n):
    edges = []
    weightRange = [i for i in range(1,n+1)]
    shuffle(weightRange)
    count = 0
    for i in range(n):
        for j in range(n):
            if i-j % 3 == 0:
                break
            edges.append(Edge(i,j,weightRange[count]))
            count+=1
            count = count % n
    return edges

def generateIncompleteGraphNegativeWeights(n):
    edges = []
    weightRange = [i for i in range(-n,n)]
    shuffle(weightRange)
    count = 0
    for i in range(n):
        for j in range(n):
            edges.append(Edge(i,j,weightRange[count]))
            count+=1
            count = count % n
    return edges
