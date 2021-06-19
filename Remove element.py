from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i <= len(nums) - 1:
            if nums[i] == val:
                # print(nums[i])
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)


obj = Solution()
print(obj.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
