# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:50:12 2020

@author: Leonardo
"""

def findAllConcatenatedWords(words):
    
    wordsSet = set(words)
    cache = {} # Optimization using dynamic programming. we cache already processed strings.
    return [word for word in words if canForm(word, wordsSet, cache)] # For each word in the words of the array. Check!


def canForm(word, wordSet, cache):
    
    if word in cache:
        
        return cache[word]    
    
    for index in range(1, len(word)):
        
        prefix = word[:index]
        suffix = word[index:]
        
        if prefix in wordSet:
            
            if suffix in wordSet or canForm(suffix, wordSet, cache):
                
                cache[word] = True
                
                return True

    return False


words = ['cat', 'cats', 'dog', 'catsdog', 'catdog']
print(findAllConcatenatedWords(words))
# Expected: catsdog catdog