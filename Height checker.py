from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        unexpected = 0
        height_sorted = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != height_sorted[i]:
                unexpected += 1
        return unexpected


obj = Solution()
print(obj.heightChecker([1, 1, 4, 2, 1, 3]))
