from _ast import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
                if maxi < counter:
                    maxi = counter
            else:
                counter = 0
        return maxi


