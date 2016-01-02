#! /usr/bin/env python
from __future__ import print_function
import unittest

""" SHORTEST COMMON SUPERSTRING
Find a shortest (possibly non-unique) superstring that contains all the given substrings
For example: ["suit","case","it"] -> "suitcase" (and also "casesuit")
             ["suit","case","it","suitcase"] -> "suitcase" (now unique)
"""
import sys
import math
import itertools

def minSuperstring(wordList):
    l=[] # List of superstrings...
    for p in itertools.permutations(wordList): # For any permutation of the word list
        i=iter(p) # Iterate in the words in that order
        candidate=next(i) # They will be added to this superstring (which is a candidate to scs)
        for w in i:
            if w in candidate: # If the word is in the candidate... need to do nothing!
                pass
            else:
                # Add the word from the left, in the position producing maximum overlapping
                bestPos=max(j*(candidate[:j] == w[-j:]) for j in range(len(w)))
                candidate=w+candidate[bestPos:]
        l.append(candidate)
    return min(l,key=len) # The shortest must be the scs

def minSuperstringCheck(self,wordList, length):
    minSuper=minSuperstring(wordList)
    self.assertEqual (len(minSuper),length) # Check with a test-provided length
    for w in wordList:
        self.assertTrue(w in minSuper) # Check substrings

class minSuperstringTest(unittest.TestCase):

    def test1(self):
        minSuperstringCheck(self,["suit","case","it"],8)
    def test2(self):
        minSuperstringCheck(self,["suit","case","it","suitcase"],8)
        minSuperstringCheck(self,["case","suit","it","suitcase"],8)
        minSuperstringCheck(self,["suitcase","case","suit","it"],8)
        minSuperstringCheck(self,["suitcase","casesuit"],12)
    def test3(self):
        minSuperstringCheck(self,["AGATTA","GATTACA","TACAGA"],10)
    def test4(self):
        minSuperstringCheck(self,["CCCTG","TGACA","CATGA"],11)
    def test5(self):
        minSuperstringCheck(self,['LOREM', 'DOLOR', 'SED', 'DO', 'MAGNA', 'AD', 'DOLORE'],14)
    def testNP(self):
        # The problem is NP-complete. You can check the increase in complexity with this test
        lLen=6
        l=list(map(chr, range(97, 97+lLen))) #["a","b",...]
        minSuperstringCheck(self,l,lLen)
    

if __name__ == "__main__":
    unittest.main()
