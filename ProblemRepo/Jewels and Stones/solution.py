# Solution for Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num_jewels = 0
        for char in stones:
            if char in jewels:
                num_jewels += 1
        return num_jewels