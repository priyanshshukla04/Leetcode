from typing import List


# [17,18,5,4,6,1]
# [18,6,6,6,1,-1]
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        if len(arr) < 2:
            return [-1]
        else:
            for a in range(i,len(arr)-1):
                arr[a] = max(arr[a+1:])
            arr[len(arr)-1] = -1
            return arr

obj = Solution()
print(obj.replaceElements([17, 18, 5, 4, 6, 1]))
# lis = [1,2,3,4,5,6,7]
# print(lis[1:])
