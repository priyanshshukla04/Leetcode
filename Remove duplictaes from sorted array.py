from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while (len(nums) - 1 > i):
            if nums[i] == nums[i + 1]:
                # print(nums[i])
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)

# class Solution {
#     public int removeDuplicates(int[] nums) {
#         int i = 0;
#         for(int j=1;j<nums.length;j++){
#             if(nums[i] != nums[j]){
#                 nums[i+1] = nums[j];
#                 i++;
#             }
#         }
#         return i+1;
#     }
# }