from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = (j-i) * min(height[i], height[j])
            # print(area)
            if maximum < area:
                maximum = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maximum


obj = Solution()
print(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
