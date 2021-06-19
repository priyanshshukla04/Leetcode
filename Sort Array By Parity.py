from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        counter1 = 0
        counter2 = 0
        while counter2 < len(A):
            if A[counter2] % 2 == 0:
                temp = A[counter1]
                A[counter1] = A[counter2]
                A[counter2] = temp
                counter2 += 1
                counter1 += 1
            else:
                counter2 += 1
        return A


obj = Solution()
print(obj.sortArrayByParity([3, 1, 2, 4]))
