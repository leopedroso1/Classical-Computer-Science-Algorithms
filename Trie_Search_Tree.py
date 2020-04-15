# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:43:53 2020

@author: Leonardo
"""

# Problem: Giving an array of elements and a prefix, return the elements of this array with all potential words which mach this prefix

# Algorithm used: Trie (Digital Tree or Prefix Tree)
# It is a kind of search tree. An ordered tree data structure is used to store a dynamic set or associative array where the key is usually strings.
# unlike binary search tree, no node in the tree stores the key associated with that node; instead, its position in the tree defines the key with which it is associated.
# All descendants of a node have a common prefix of the string associated with that node, and the root is associated with the empity string. Keys tend to be associated with leaves, though some inner nodes may correspond to keys of interest. 
# Hence, keys are not necessarily associated with every node. For the space-optimized see compact prefix tree

# Example: for prefix 'do' and an array ['dog', 'dark', 'cat', 'door', 'dodge'] an expected answer is dog / door / dodge 
# A tree for this array would be:

#level 1                  EMPTY
#level 2               D        C
#level 3             O            A
#level 4         D  G  O            T
#level 5       G         R
#level 6     E

class Node:
    
    def __init__(self, children, isWord):
        
        self.children = children
        self.isWord = isWord
        

class Solver:
    
    def __init__(self):
        
        self.trie = None
    
    def buildTrie(self, words): # Build the Trie Search Tree given the words
        
        self.trie = Node({}, False)
        
        for word in words:
            
            current = self.trie
            
            for char in word:
                
                if not char in current.children:

                    current.children[char] = Node({}, False)
                        
                current = current.children[char]
            
            current.isWord = True
                
    def autoComplete(self, prefix): # Autocomplete the prefix given the word tree pre-settled
        
        current = self.trie
        
        for char in prefix:
            
            if not char in current.children:
                
                return []
            
            current = current.children[char]
            
        return self._findWordsFromNode(current, prefix)
    
    def _findWordsFromNode(self, node, prefix):
        
        words = []
        
        if node.isWord:
            
            words += [prefix]
            
        for char in node.children:
            
            words += self._findWordsFromNode(node.children[char], prefix + char) # Recursion to run the tree searchin all characters

        return words


s = Solver()
s.buildTrie(['dog','dark','cat','door','dodge'])
print(s.autoComplete('do'))
# Possible solution: dog, door, dodge









