# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:05:02 2020

@author: Leonardo
"""

import sys 

# Dijkstra algorithm is used to find the shortest path in a graph 
# Given a graph and a source vertex in the graph, find shortest paths from source to all vertices in the given graph.

# Let's create a graph first!!
class Graph:
    
    def __init__(self, vertices):
        
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    
    
    def printSolution(self, dist):
        
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print (node, "\t", dist[node])

    # Utilitary function to find the vertex with minimum distance value, from the set of vertices not yet included in the shortest path tree            
    def minDistance(self, dist, sptSet):
        
        # Initialize minimum distance from next node
        min = sys.maxint
        
        # Search not nearest vertex not in the shortest path tree
        for v in range(self.V):

            if dist[v] < min and sptSet[v] == False:
                
                min = dist[v]
                min_index = v
        
        return min_index
        
    # Dijkstra path finder single source. Shortest path algorithm for a graph using adjacency matrix representation
    def dijkstra_Pathfinder(self, src):
        
        dist = [sys.maxint] *  self.V # Array with all calculated distances
        dist[src] = 0 # start the distances with 0 in the path finder
        sptSet = [False] * self.V # control set
        
        for cout in range(self.V):
            
            # Catch the minimum distance vertex from the set of vertices not yet processed. 
            # u is = to src in the first iteration!
            u = self.minDistance(dist, sptSet)
            
            # Put the minimum distance vertex in the shortest path tree and set True as calculated
            sptSet[u] = True

            # Update distance (dist) value of the adjacent vertices of the picked vertex only if the current
            # distance is greater than new distance and the vertex in not in the shortest path tree
            for v in range(self.V):
     
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    
                    dist[v] = dist[u] + self.graph[u][v]
                    
        self.printSolution(dist)
            
        
        

g = Graph(9) # Initialize a graph with 9 nodes
# print(g.graph) >> Remove the comment for reference

# Populate the graph with all distances between nodes.
# In this matrix each row is a node 0 - 8 (9 nodes) and each column is the distance
# For example: Node 0 is the first row. This node has the distance of 4 with the Node 1 (2º column - column[1]), and distance of 8 with the Node 7 (8º column - column[7])

g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
           ]; 
  
g.dijkstra_Pathfinder(0) 

