"""
LeetCode Problem 2411: Smallest Subarrays with Maximum Bitwise OR
Solution by Eric Li
"""

from typing import List
import heapq

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        '''
        Go in reverse order of the array and collect the bits of the value.
        Update all bits that this value can represent to be represented by this value.
        Take the largest index representing a bit minus the curren tindex.
        '''
        
        output = [0 for _ in range(len(nums))]
        bitToIdxDict = {} # Track which index is representing each bit
        idxToBitsDict = {} # Track which bit(s) the index is representing
        furthestIdx = [] # Track the furthest index that needs to be representing the max BITOR
        for idx in range(len(nums) - 1, -1, -1):
            val = nums[idx]
            bitIndex = 0
            while val:
                # Check if value can represent bit
                if val & 1:
                    if bitIndex in bitToIdxDict:
                        # Replace the previous rep for this bit and update furthestIdx
                        prevBitIdx = bitToIdxDict[bitIndex]
                        if len(idxToBitsDict[prevBitIdx]) == 1:
                            del idxToBitsDict[prevBitIdx]
                            while furthestIdx and -furthestIdx[0] not in idxToBitsDict:
                                heapq.heappop(furthestIdx)
                        else:
                            idxToBitsDict[prevBitIdx].remove(bitIndex)
                    
                    # Add as rep of bit
                    bitToIdxDict[bitIndex] = idx
                    if idx in idxToBitsDict:
                        idxToBitsDict[idx].add(bitIndex)
                    else:
                        idxToBitsDict[idx] = set([bitIndex])
                        heapq.heappush(furthestIdx, -idx)
                val >>= 1
                bitIndex += 1

            # output is the length from the furthest index to the current index
            output[idx] = -furthestIdx[0] - idx + 1 if len(furthestIdx) > 0 else 1
        return output