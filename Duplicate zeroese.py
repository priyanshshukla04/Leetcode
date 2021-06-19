from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] == 0:
                for j in range(len(arr) - 1, i, -1):
                    arr[j] = arr[j - 1]
                i += 1
            i += 1


