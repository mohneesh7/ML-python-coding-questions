# Solution for Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # case check for single element
        # if len(s) <= 1:
        #     return

        left = 0
        right = len(s) - 1
        while left < right:
            # temp = s[left]
            # s[left] = s[right] 
            # s[right] = temp

            # better way to swap
            s[left], s[right] = s[right], s[left]
            left += 1
            right -=1
