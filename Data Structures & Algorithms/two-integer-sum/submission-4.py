class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left in range(len(nums)):
            right = left+1
            while right < len(nums):
                tar = nums[left]+nums[right]
                if tar == target:
                    return [left,right]
                right += 1