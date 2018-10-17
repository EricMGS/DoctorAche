#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#SPELL CHECKER
#Author: ericmgs
#Date: oct 16, 2018

#REFERENCE: http://www.catalysoft.com/articles/StrikeAMatch.html
#SIMILAR ALGORITHMS: SOUNDEX, EDIT DISTANCE, LONGEST COMMON SUBSTRING

def letterPairs(string):
    numPairs = len(string) - 1
    pairs = []
    
    for i in range(numPairs):
        pairs.append(string[i : i + 2])
        
    return pairs

def wordLetterPairs(string):
    words = string.split()
    pairs = []
    
    for w in words:
        pairs += letterPairs(w)
        
    return pairs

def compareStrings(str1, str2):
    pairs1 = wordLetterPairs(str1.upper())
    pairs2 = wordLetterPairs(str2.upper())
    
    intersection = 0
    union = len(pairs1) + len(pairs2)
    
    for p1 in pairs1:
        for p2 in pairs2:
            if p1 == p2:
                intersection += 1
                del pairs2[pairs2.index(p2)]
                break
            
    return  (2 * intersection) / union
    
def spellChecker(string, wordlist):
    class Match:
        def __init__(self):
            self.word = ''
            self.probability = 0
    
    match = Match()
    for word in wordlist:
        probability = compareStrings(word, string) 
        if probability > match.probability:
            match.word = word
            match.probability = probability
    
    if match.probability == 0:
        return None
    
    return match.word