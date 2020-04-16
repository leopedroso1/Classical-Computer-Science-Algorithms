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
        
    def bfs_Search(self, s):
        
        # Mark all vertices already visited
        visited = [False] * len((self.graph))
        
        # Create a queue for BFS (Remember: We will navigate through levels in the graph so imagine a node A with 2 children B and C. We will store in de queue all levels we are looking the path)
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
        
        while queue:
            
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end = " ")
            
            # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                
                if visited[i] == False:  
                    
                    queue.append(i)

                    visited[i] = True

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print(g.graph)

## Depth First Search >> nodes goes deep asking for neighbors if they have a path to another node. It is an recursive algorithms and is an exhaustive methodology for asking like a broadcasting
print("Executing BFSS from (starting from vertex 2)") 
g.bfs_Search(2) 




## Breadth Frist Search >> Goes broad (to neighbors) before going deep. It's also an recursive algorithm. You can use a queue for iteration
#def bfs_Search():

