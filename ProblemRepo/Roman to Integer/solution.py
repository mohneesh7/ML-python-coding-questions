# Solution for Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        num_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        for rom in range(len(s)-1):
            if num_dict[s[rom]] < num_dict[s[rom + 1]]:
                total -= num_dict[s[rom]]
            else:
                total += num_dict[s[rom]]
        
        total += num_dict[s[-1]]
        return total