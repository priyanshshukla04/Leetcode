from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in nums:
            square = i * i
            new_list.append(square)
        new_list.sort()
        print(new_list)
        # return new_list.sort()
obj = Solution()
obj.sortedSquares([-4,-1,0,3,10])