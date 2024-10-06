# Solution for Two Sum II - Input Array Is Sorted

class Solution:
    def diff_bw_nums(self, a: int, b: int) -> int:
        return a-b

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            
            if self.diff_bw_nums(target,numbers[right]) == numbers[left]:
                return [left + 1, right + 1]
            
            if self.diff_bw_nums(target,numbers[right]) == numbers[left + 1]:
                return [left + 2, right + 1]
            
            if (self.diff_bw_nums(target,numbers[right]) > numbers[left]) and (self.diff_bw_nums(target,numbers[right]) > numbers[left + 1]):
                left += 1
            if (self.diff_bw_nums(target,numbers[right]) > numbers[left]) and (self.diff_bw_nums(target,numbers[right]) < numbers[left + 1]) or (self.diff_bw_nums(target,numbers[right]) < numbers[left]):
                right -= 1

        