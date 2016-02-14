# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import *

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."
    txt = open('E:\Python\mystuff\Data Science\ProblemSet5\ProblemSet5\\' + str(mapFilename), 'r')
    mit = WeightedDigraph()
    parsed = []
    for line in txt:
        parsed.append(line.split())
    for package in parsed:
        first = Node(package[0])
        second = Node(package[1])
        try:
            mit.addNode(first)
            mit.addNode(second)
            mit.addEdge(WeightedEdge(first, second, package[2], package[3]))
        except ValueError:
            try:
                mit.addNode(first)
                mit.addEdge(WeightedEdge(first, second, package[2], package[3]))
            except ValueError:
                try:
                    mit.addNode(second)
                    mit.addEdge(WeightedEdge(first, second, package[2], package[3]))
                except ValueError:
                    mit.addEdge(WeightedEdge(first, second, package[2], package[3]))
       # try:
           # mit.addNode(second)
           # mit.addEdge(WeightedEdge(first, second, package[2], package[3]))
       # except ValueError:
            #mit.addEdge(WeightedEdge(first, second, package[2], package[3]))
        
            
    return mit
       
#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#
def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(Node(path[i]))
        else:
            result = result + str(Node(path[i])) + '->'
    return result

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors, path=[]):
    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO

#    path = path + [Node(start)]
 #   print 'Current dfs path:', printPath(path)
  #  if Node(start) == Node(end):
   #     outside = 0
    #    distance = 0
     #   for i in range(len(path)):
      #      for k in digraph.edges[Node(path[i])]:
       #         try:
        #            if k[0] == Node(path[i+1]):
         #               distance += k[1][0]
          #              outside += k[1][1]
           #     except IndexError:
            #        result = meetConstraints(distance, outside, maxTotalDist, maxDistOutdoors)
             #       if result == True:
              #          return path
               #         break
                #    else:
                 #       raise ValueError
   # for node in digraph.childrenOf(Node(start)):
    #    if Node(node[0]) not in path :
     #       newPath = bruteForceSearch(digraph, Node(node[0]), end, maxTotalDist, maxDistOutdoors, path)
      #      if newPath != None:
       #         return newPath
                
   # return None
    
    #initPath = [str(start)]
    #q.append(initPath)
    #while len(q) != 0:
     #   tmpPath = q.pop(0)
      #  lastNode = tmpPath[len(tmpPath) - 1]
       # print 'Current dequeued path: ', printPath(tmpPath)
        #if lastNode == str(end):
         #   for i in range(len(tmpPath)):
          #      for k in mitmap.edges[Node(tmpPath[i])]:
           #         try:
            #            if k[0] == Node(test[i+1]):
             #               distance += k[1][0]
              #              outside += k[1][1]
               #     except IndexError:
                #        result = meetConstraints(distance, outside, maxTotalDist, maxDistOutdoors)
                 #       if result == True:
                  #          return tmpPath
                   #     else:
                    #        raise ValueError
                      
                  #  for linkNode in graph.childrenOf(lastNode):
                   #         if linkNode not in tmpPath:
                    #                newPath = tmpPath + [linkNode]
                     #               q.append(newPath)
           # return None
#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#

def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    trash = []
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    
    def getEdgeTotalDistances(src, dest, digraph):
        for i in digraph.edges[Node(str(src))]:
            if Node(i[0]) == Node(str(dest)):
                return int(i[1][0])
    def getEdgeOutdoorDistances(src, dest, digraph):
        for i in digraph.edges[Node(str(src))]:
            if Node(i[0]) == Node(str(dest)):
                return int(i[1][1])
        
    def getPathDistance(path):
        distance, outDistance = 0, 0
        if path == None:
            return maxTotalDist, maxDistOutdoors
        for i in range(len(path)-1):
            src, dest = path[i], path[i+1]
            distance += getEdgeTotalDistances(src, dest, digraph)
            outDistance += getEdgeOutdoorDistances(src, dest, digraph)
        return int(distance), int(outDistance)

    def DFS(digraph, start, end, maxTotalDist, maxDistOutdoors, path=[], shortest=None, \
            currentDistance = 0, currentOutDistance = 0):
        
        path = path +[Node(start)]
        if Node(start) == Node(end):
            return path
        
        for node in digraph.childrenOf(Node(start)):
            if Node(node[0]) not in path:
                #If we don't have a shortest list yet, or if our current path is shorter than our shortest list.
                #If the path we are currently on is longer than the shortest path we have found, there is no point in going down
                #The path any further.
                if shortest == None or len(path)<len(shortest):
                    if currentDistance + getEdgeTotalDistances(start, node[0], digraph) <=maxTotalDist and \
                       currentOutDistance + getEdgeOutdoorDistances(start, node[0], digraph) <= maxDistOutdoors:
                        
                        currentDistance += getEdgeTotalDistances(start, node[0], digraph)
                        currentOutDistance += getEdgeOutdoorDistances(start, node[0], digraph)
                        #print path
                        newPath = DFS(digraph, Node(node[0]), end, maxTotalDist, maxDistOutdoors, \
                                      path, shortest, currentDistance, currentOutDistance)
                        
                        if newPath != None:
                            shortest = newPath
        return shortest
            
    result = DFS(digraph, start, end, maxTotalDist, maxDistOutdoors)
    return result
    

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
#     Test cases
     mitMap = load_map("mit_map.txt")
     print isinstance(mitMap, Digraph)
     print isinstance(mitMap, WeightedDigraph)
     print 'nodes', mitMap.nodes
     print 'edges', mitMap.edges


     LARGE_DIST = 1000000

     #Test case 1
     print "---------------"
     print "Test case 1:"
     print "Find the shortest-path from Building 32 to 56"
     expectedPath1 = ['32', '56']
#     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
     dfsPath1 = directedDFS(mitMap, Node('32'), Node('56'), LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath1
#     print "Brute-force: ", brutePath1
     print "DFS: ", dfsPath1
     print "Correct? DFS: {0}".format(str(Node(expectedPath1)) == str(Node(dfsPath1)))

#     Test case 2
     print "---------------"
     print "Test case 2:"
     print "Find the shortest-path from Building 32 to 56 without going outdoors"
     expectedPath2 = ['32', '36', '26', '16', '56']
     #brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
     dfsPath2 = directedDFS(mitMap, Node('32'), Node('56'), LARGE_DIST, 0)
     print "Expected: ", expectedPath2
     #print "Brute-force: ", brutePath2
     print "DFS: ", dfsPath2
     print "Correct? DFS: {0}".format(Node(expectedPath2) == Node(dfsPath2))

#     Test case 3
     print "---------------"
     print "Test case 3:"
     print "Find the shortest-path from Building 2 to 9"
     expectedPath3 = ['2', '3', '7', '9']
#     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
     dfsPath3 = directedDFS(mitMap, Node('2'), Node('9'), LARGE_DIST, LARGE_DIST)
     print "Expected: ", expectedPath3
#     print "Brute-force: ", brutePath3
     print "DFS: ", dfsPath3
     print "Correct? DFS: {0}".format(Node(expectedPath3) == Node(dfsPath3))

#     Test case 4
     print "---------------"
     print "Test case 4:"
     print "Find the shortest-path from Building 2 to 9 without going outdoors"
     expectedPath4 = ['2', '4', '10', '13', '9']
#     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
     dfsPath4 = directedDFS(mitMap, Node('2'), Node('9'), LARGE_DIST, 0)
     print "Expected: ", expectedPath4
#     print "Brute-force: ", brutePath4
     print "DFS: ", dfsPath4
     print "Correct? DFS: {0}".format(Node(expectedPath4) == Node(dfsPath4))

#     Test case 5
     print "---------------"
     print "Test case 5:"
     print "Find the shortest-path from Building 1 to 32"
     expectedPath5 = ['1', '4', '12', '32']
#     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
     dfsPath5 = directedDFS(mitMap, Node('1'), Node('32'), LARGE_DIST, LARGE_DIST)
     print "Expected: ", expectedPath5
#     print "Brute-force: ", brutePath5
     print "DFS: ", dfsPath5
     print "Correct? DFS: {0}".format(Node(expectedPath5) == Node(dfsPath5))

#     Test case 6
     print "---------------"
     print "Test case 6:"
     print "Find the shortest-path from Building 1 to 32 without going outdoors"
     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
     dfsPath6 = directedDFS(mitMap, Node('1'), Node('32'), LARGE_DIST, 0)
     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
     print "DFS: ", dfsPath6
     print "Correct? DFS: {0}".format(Node(expectedPath6) == Node(dfsPath6))

#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr
