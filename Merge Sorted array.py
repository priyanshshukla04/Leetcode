from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        point1 = m - 1
        point2 = n - 1
        leng = m + n - 1
        while (point2 >= 0):
            if point1 >= 0 and nums1[point1] > nums2[point2]:
                nums1[leng] = nums1[point1]
                point1 -= 1;
                leng -= 1
            else:
                nums1[leng] = nums2[point2]
                leng -= 1;
                point2 -= 1


obj = Solution()
obj.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
