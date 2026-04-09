class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

      for lp in range(len(nums)):
        rp = lp+1
        while rp < len(nums):
            t = nums[lp]+nums[rp]
            if t == target:
                return [lp,rp]
            rp += 1