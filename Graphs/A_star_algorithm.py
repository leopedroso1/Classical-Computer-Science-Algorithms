# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:38:37 2020

@author: Leonardo
"""

# f = g + h

# f = is the total cost of the node
# g = is the distance between the current node and the start node
# h = heuristic >> estimated distance from the current node to the end node


# A* Algorithm x Djikstra:
# Dijkstra’s algorithm It has no idea which node is ‘best’, so it calculates paths for all nodes them all. 
# The A*, once we get past the obstacle, the algorithm prioritizes the node with the lowest f and the ‘best’ chance of reaching the end.

# Step by Step of A* algorithm

# 1. Add starting square (node) to the open list
# 2. Repeat the following sentences:
#   a. Look for the lowest 'f' cost square on the open list. We refer to this as the current square
#   b. Switch it to the closest list
#   c. For each 8 squares adjacent to this current square...
#      > If it is not walkable of if it is not on the closed list, ignore it. Otherwise do the following steps
#      > If it is not on the open list, add it to the open list. Make the current square the parent of this square. Record f, g, and h costs of the square
#      > If it is on the open list already, check to see if this path to that square is better, using G cost as the measure.
#           A lower G cost means that this is a better path. If so, change the parent of the square to the current square, and recalculate the g and f scores of the square.
#           If you are keeping your open list sorted by F score, you may need to resort the list to account for the change           

#   d. Stop when...
#       > Add the target square to the closed list, in which case the path has been found, or
#       > Fail to find the target square, and the open list is empty. In this case, there is no path

# 3. Save the path. Working backwards from the target square, go from each square to its parent until you reach the starting square. That is your path

# Class for assembly Nodes and A* pathfinding
class Node():
    
    def __init__(self, parent=None, position=None):
        
        self.parent = parent
        self.position = position
        
        self.g = 0
        self.h = 0
        self.f = 0
        

    def __eq__(self, other):
        
        return self.position == other.position
    
# Returns a list of tuples as a path from the given start to the given end in the given maze
def a_star(maze, start, end):
    
    # Create a Start and End node
    start_node = Node(None, start)

    start_node.g = 0
    start_node.f = 0
    start_node.h = 0

    end_node = Node(None, end)
    
    end_node.g = 0
    end_node.f = 0
    end_node.h = 0
    
    # Start open and closed list:
    open_list = []
    closed_list = []
        
    # Add start node
    open_list.append(start_node)
    
    # Loop until find the end
    while len(open_list) > 0:
        
        # get current node
        current_node = open_list[0]
        current_index = 0
        
        for index, item in enumerate(open_list): # enumerate >> returns an object with iterable object. Example: given a list ['spring', 'summer', 'fall', 'winter']  it will return a tuple with iterators [(0, 'spring'), (1, 'summer') ...]
            
            if item.f < current_node.f:
                
                current_node = item
                current_index = index
        
        # Pop current off open list, add to closed list
        open_list.pop(current_index) # if checked Pop the current
        closed_list.append(current_node) # append at closed case
        
        # Found the goal!
        if current_node == end_node:

            path = []
            current = current_node
            
            while current is not None:
                
                path.append(current.position) # append all positions calculated in the path tracker
                current = current.parent # set the current as a parent to reverse the list
            
            return path[::-1] # Return reversed path
        
        # Generate children        
        children = []
        
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares
            
            # Get node position >> Add to the current position the next blocks to be checked
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            
            # Make sure within range
            if node_position[0] > (len(maze) -1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                
                continue
            
            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:

                continue
            
            # Create a new node and append
            new_node = Node(current_node, node_position)
            children.append(new_node)
            
        # Loop through children
        for child in children:
            
            # Child is on the closed list
            for closed_child in closed_list:
                
                if child == closed_child:
                    
                    continue
                
            # create the f, g, h values
            child.g = current_node.g + 1
            child.f = child.g + child.h
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            

            # Child is already in the open list
            for open_node in open_list:
                
                if child == open_node and child.g > open_node.g:
                    
                    continue
                
            # add the child to the open list
            open_list.append(child)
            



maze =     [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start = (0, 0)
end = (7, 6)

path = a_star(maze, start, end)    
print(path)        