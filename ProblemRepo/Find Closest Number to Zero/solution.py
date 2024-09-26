class Solution:
    def diff_of_num(self, num):

        if num <= 0:
            return -num
        else:
            return num

    def findClosestNumber(self, nums):
        closest = nums[0]
        for x in nums:

            # check if its closest
            if self.diff_of_num(x) < self.diff_of_num(closest):
                closest = x
            
            # if x == closest, return max(x,closest) yet to optimized
            if self.diff_of_num(x) == self.diff_of_num(closest):
                closest = max(x,closest)
        return closest