class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        i = 0
        nums = sorted(nums)
        print(nums)
        while i < len(nums)-1:
            print(nums[i], nums[i+1], nums[i-1])
            if nums[i] != nums[i+1] and nums[i] != nums[i-1]: 
                return nums[i]
            i += 1
        last = nums.pop()
        if last not in nums:
            return last
        return 

        
        