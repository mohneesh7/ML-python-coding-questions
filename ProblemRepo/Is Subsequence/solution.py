# Solution for Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: 
        if s == '':
            return True
            
        s_list = list(s)
        for char in t:
            if s_list != [] and char == s_list[0]:
                s_list.pop(0)

        if s_list == []:
            return True
        else:
            return False