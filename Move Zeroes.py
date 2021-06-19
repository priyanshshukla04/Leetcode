from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> list[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter1 = 0
        counter2 = 0
        while counter2 < len(nums) :
            if nums[counter2] != 0:
                temp = nums[counter1]
                nums[counter1] = nums[counter2]
                nums[counter2] = temp
                counter1 += 1
                counter2 += 1
            else:
                counter2 += 1
        return nums

obj = Solution()
print(obj.moveZeroes([0, 0, 1]))
