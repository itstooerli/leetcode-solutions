"""
LeetCode Problem 1233: Remove Sub-Folders from the Filesystem
Solution by Eric Li
"""

from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        '''
        Should be easier to sort and identify parent directories.
        Then, if subsequent child directories have a parent already, then remove it.
        Otherwise, keep the child.
        '''
        folder.sort()
        parent_folders = set()
        output = []
        for filepath in folder:
            shouldKeep = True
            idx = 1 # filepath always starts with /
            while idx < len(filepath):
                if filepath[idx] != "/":
                    idx += 1
                    continue
                
                currPath = filepath[0:idx]
                if currPath in parent_folders:
                    shouldKeep = False
                    break
                
                idx += 1
            
            if shouldKeep:
                parent_folders.add(filepath)
                output.append(filepath)

        return output