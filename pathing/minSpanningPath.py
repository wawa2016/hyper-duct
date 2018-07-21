from shapely.geometry import Point
from itertools import combinations
import networkx as nx

bldg = [
   [
    { "name": "Space-101",
    "location": [1.2, 3.0, 1.0],
    "cfm": 100,
    },
    { "name": "Space-102",
    "location": [2, 5.0, 1.0],
    "cfm": 200,
     },
    { "name": "Space-103",
    "location": [4, 1.0, 1.0],
    "cfm": 250,
     },
    { "name": "Space-106",
    "location": [6, 3.0, 1.0],
    "cfm": 350,
     },
   ]
]

# lstOPoints = [ (0,3),(2,5),(4,8),(7,3), (8,8) ]

def GetRoutes(aLevel):
    G = nx.Graph()
    for sp1,sp2 in combinations(aLevel, 2):
        i,j = tuple(sp1['location']), tuple(sp2['location'])
        dist = Point(i[0], i[1]).distance(Point(j[0], j[1]))
        print(dist)
        if(dist > 0):
            print(sp1, sp2)
            G.add_edge(sp1['name'],sp2['name'] , weight=dist)
    print(G)
    span = nx.minimum_spanning_tree(G)
    return span
    

#this adds the load for each point along all edges in the path
def AddCFMToRoute(lvl, span, rootnode):
    for n in range(0,len(lvl)):
        destSpace = lvl[n]
        print(destSpace['name'])
        if(n==rootnode):
            continue
        pth = next(nx.shortest_simple_paths(span, source=lvl[rootnode]['name'], target=destSpace['name']))
        
        for i in range(1,len(pth)):
            print("i: ", i)
            if loadVar not in span[pth[i-1]][pth[i]]:
                span[pth[i-1]][pth[i]][loadVar] = 0
            span[pth[i-1]][pth[i]][loadVar] += destSpace['cfm']
            print(span[pth[i-1]][pth[i]])

    return span

rootnode = 3
loadVar = 'cfm'

spanningTree = GetRoutes(bldg[0])
spanWithLoads = AddCFMToRoute(bldg[0], spanningTree, rootnode)

