# Solution for Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = []
        min_length = min(len(word1), len(word2))
        if len(word1) != len(word2):
            if len(word1) > len(word2):
                temp_string = word1[min_length:]
            else:
                temp_string = word2[min_length:]
        else:
            temp_string = ''
        
        for x in range(min_length):
            new_string.append(word1[x])
            new_string.append(word2[x])
        
        new_string = ''.join(new_string) + temp_string

        return new_string
        