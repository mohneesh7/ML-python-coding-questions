# Solution for Contains Duplicate

class Solution:
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        # import numpy as np
        # from collections import Counter

        # counter = Counter(nums)
        # for x in counter:
        #     if counter[x] > 1:
        #         return True
        # return False
        
        # above approach is taking 437 ms too slow.

        return (len(set(nums)) != len(nums)) # still takes 404 ms
        # return ( len(np.unique(nums)) != len(nums)) # takes 613 ms useless using numpy here