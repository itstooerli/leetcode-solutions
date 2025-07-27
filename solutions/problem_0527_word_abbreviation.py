"""
LeetCode Problem 527: Word Abbreviation
Solution by Eric Li
"""

from typing import List

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def abbreviate(word):
            '''
            Given a word, return the initial abbreviation defined as
            1. the first character
            2. the number of characters in between
            3. the last character
            '''
            prefix = word[0]
            suffix = word[-1]
            body = str(len(word) - 2) if len(word) >= 2 else ""
            return prefix + body + suffix

        def extendAbbreviation(word, abbr):
            '''
            Given a word and its previous abbreviation, return the new abbreviation
            increasing the prefix by 1. This will return the full word if no more
            body count left.
            '''
            abbrBodyCount = getBodyCount(abbr)
            prefixLength = len(word) - 1 - abbrBodyCount
            prefix = word[0:prefixLength+1]
            suffix = word[-1]
            newBodyCount = abbrBodyCount - 1
            body = str(newBodyCount) if newBodyCount > 0 else ""
            newAbbr = prefix + body + suffix
            return newAbbr

        def getBodyCount(abbr):
            '''
            Given an abbreviation, return the length of abbreviated portion.
            '''
            bodyCount = ""
            numIdx = len(abbr) - 2
            while abbr[numIdx].isdigit():
                bodyCount = abbr[numIdx] + bodyCount
                numIdx -= 1
            return int(bodyCount) if bodyCount.isdigit() else 0

        def resolveConflict(word, abbr, abbrToWordDict, wordToAbbrDict):
            '''
            Given a word and abbreviation, check if the abbreviation would conflcit
            with an existing abbreviation. If not, add it to the dictionary. Otherwise,
            resolve the conflicting word and the given word's conflict.
            '''
            # If abbreviation isn't in the dictionary, then just add it.
            if abbr not in abbrToWordDict:
                abbrToWordDict[abbr] = word
                wordToAbbrDict[word] = abbr
                return
            
            # Otherwise we have a conflict we need to resolve.
            # Resolve previous word first, but note that it might previously have been abbreviated
            # so in that instance only abbreviate if in conflict with latest abbreviation.
            conflictWord = abbrToWordDict[abbr]
            conflictWordAbbr = wordToAbbrDict[conflictWord]
            if conflictWordAbbr == abbr:
                conflictWordNewAbbr = extendAbbreviation(conflictWord, conflictWordAbbr)
                resolveConflict(conflictWord, conflictWordNewAbbr, abbrToWordDict, wordToAbbrDict)

            # Resolve current word next
            newAbbr = extendAbbreviation(word, abbr)
            resolveConflict(word, newAbbr, abbrToWordDict, wordToAbbrDict)
        
        abbrToWordDict = {}
        wordToAbbrDict = {}
        for word in words:
            resolveConflict(word, abbreviate(word), abbrToWordDict, wordToAbbrDict)

        output = []
        for word in words:
            abbr = wordToAbbrDict[word]
            if len(abbr) >= len(word):
                output.append(word)
            else:
                output.append(abbr)
        
        return output