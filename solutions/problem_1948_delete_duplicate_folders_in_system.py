"""
LeetCode Problem 1948: Delete Duplicate Folders in System
Solution by Eric Li
"""

from typing import List
from bisect import bisect_left

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        class CustomNode:
            def __init__(self, value, idx):
                self.value = value
                self.idx = idx
                self.children = []
                self.childrenValues = []
            
            def addChildren(self, child):
                # Find sorted index
                idx = bisect_left(self.childrenValues, child.value)
                # Insert in both lists
                self.children.insert(idx, child)
                self.childrenValues.insert(idx, child.value)
        
            def getChildrenInfo(self, allKeys):
                key = ""
                relevantIdx = [self.idx]
                for child in self.children:
                    childInfo = child.getChildrenInfo(allKeys)
                    # If child is an leaf, we'll take care of its index for it
                    if childInfo[0] == "/":
                        relevantIdx.append(childInfo[2])
                    # Create key based on value_childKeys
                    key += childInfo[1] + "_" + childInfo[0]
                # Only add non-leafs to allKeys
                if key:
                    allKeys.append((key, self.value, relevantIdx))
                # Add "/" as separator between siblings
                key += "/"
                return (key, self.value, self.idx)

        # Sort by file path length, starting with the shortest, which should be closest to root
        paths.sort(key = lambda x : len(x))
        
        # Reconstruct file structure to verify children
        root = CustomNode("root", -1)
        allCustomNodes = {} # Stores all children nodes -- key: concatenated folder path, value: CustomNode
        for pathIdx, path in enumerate(paths):
            nodeKey = ""
            for folderIdx in range(len(path) - 1):
                nodeKey += path[folderIdx]
            parentFolder = allCustomNodes[nodeKey] if nodeKey else root

            currFolder = path[-1]
            currNode = CustomNode(currFolder, pathIdx)
            parentFolder.addChildren(currNode)
            nodeKey += currFolder
            allCustomNodes[nodeKey] = currNode
        
        # Get all children info
        allKeys = []
        root.getChildrenInfo(allKeys)
        
        # Find duplicates and mark any for deletion
        markForDeletion = set()
        uniquePaths = {}
        for key in allKeys:
            if key[0] in uniquePaths:
                markForDeletion.update(uniquePaths[key[0]])
                markForDeletion.update(key[2])
            else:
                uniquePaths[key[0]] = key[2]

        # Delete any duplicate folders
        output = []
        for idx in range(len(paths)):
            if idx not in markForDeletion:
                output.append(paths[idx])

        return output