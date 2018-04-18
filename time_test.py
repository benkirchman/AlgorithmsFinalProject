#!/usr/bin/env python3

import matplotlib.pyplot as plt
import shortest_path as sp
import generator as gen
import time
import atexit

def generatePlot(generator, title):
    ns     = []
    times  = []
    min_i  = 5
    max_i  = 100
    iFactor = 1

    for i in range( min_i, max_i ):
        n = i * iFactor
        edges = generator(n)

        t1 = time.time()
        #for edge in edges:
            #print(edge.asString())
        m = sp.getShortestPath(edges, range(n))
        #print(str(m))
        t2 = time.time()
        td = t2 - t1

        #print( "%d %d %s" % ( i, n, td ) )
        ns.append( n )
        times.append( td )

    plt.plot( ns, times, label= title)


plt.xlabel('input size')
plt.ylabel('time (s)')
plt.title("shortest_path problem solving time vs input size")
plt.grid(True)
#plt.savefig(title + str(time.time()) + ".png")

generatePlot(gen.generateCompleteGraphRandomWeights, "complete")
generatePlot(gen.generateIncompleteGraphRandomWeights, "incomplete")
generatePlot(gen.generateCompleteGraphNegativeWeights, "negative")
generatePlot(gen.generateCycle, "cycle")

plt.legend(loc='upper left')
plt.show()
