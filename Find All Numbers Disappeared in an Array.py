from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        normal_list = [i for i in range(1, len(nums) + 1)]
        normal_list = set(normal_list)
        print(normal_list)

        given_list = set(nums)
        print(given_list)
        # return [normal_list - given_list]


obj = Solution()
print(obj.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
