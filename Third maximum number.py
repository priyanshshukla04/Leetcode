from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = list(set(nums))
        maxi = None   #[1,2,3]
        second_max = None
        third_max = None
        for i in range(len(arr)):
            if arr[i] == maxi or arr[i] == second_max or arr[i] == third_max:
                continue
            if maxi == None or arr[i] > maxi:
                third_max = second_max
                second_max = maxi
                maxi = arr[i]
            elif second_max == None or arr[i] > second_max:
                third_max = second_max
                second_max = arr[i]
            elif third_max == None or arr[i] > third_max:
                third_max = arr[i]
        if len(arr) < 3:
            return maxi
        else:
            return third_max


obj = Solution()
print(obj.thirdMax([2,2,3,1]))