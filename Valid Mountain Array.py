from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        val1 = False
        val2 = False
        j = len(arr) - 1
        if len(arr) < 3:
            return False
        maxi = max(arr)
        index_max = arr.index(maxi)
        for b in range(index_max, i, -1):
            if arr[b - 1] >= arr[b]:
                return False
            else:
                val1 = True
        for a in range(index_max, j):
            if arr[a + 1] >= arr[a]:
                return False
            else:
                val2 = True
        if val1 and val2:
            return True
        else:
            return False

obj = Solution()
print(obj.validMountainArray([3, 5, 5]))
# for i in range(1,5):
#     print(i)
