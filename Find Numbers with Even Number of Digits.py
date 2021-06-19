from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for i in nums:
            i = str(i)
            if len(i) % 2 == 0:
                counter += 1
        return counter

