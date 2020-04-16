# -*- coding: utf-8 -*-v
"""
Created on Thu Apr 16 12:46:19 2020

@author: Leonardo

"""

from collections import defaultdict 

class Graph:
    
    def __init__(self):
        
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        
        self.graph[u].append(v)
        
    def dfs_Util(self, v, visited):
        
        # Mark current node visited
        visited[v] = True
        print(v, end = ' ')
        
        # Recurr for all vertices adjacent to this vertex
        for i in self.graph[v]:

            if visited[i] == False:
                
                self.dfs_Util(i, visited)
                
    def dfs_Search(self, v):
        
        # Mark all vertices as not visited 
        visited = [False] * (len(self.graph))
        
        # calls the recursive helper function
        self.dfs_Util(v, visited)

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print(g.graph)
print("Following is DFS from (starting from vertex 2)") 
g.dfs_Search(2) 



## Depth First Search >> nodes goes deep asking for neighbors if they have a path to another node. It is an recursive algorithms and is an exhaustive methodology for asking like a broadcasting

## Breadth Frist Search >> Goes broad (to neighbors) before going deep. It's also an recursive algorithm. You can use a queue for iteration
#def bfs_Search():
#
#    pass
#
## A Star >>
#def a_star():
#
#    pass
#    
## Dijkstra >>  
#def disjkstra():
#    
#    pass