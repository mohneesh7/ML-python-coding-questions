# Solution for Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_list = list(s)
        s = ''.join([x for x in s_list if x.isalnum()])
        return s == s[::-1]
        