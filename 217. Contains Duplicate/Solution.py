class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in hash:
                return True
            hash[nums[i]] = "exists"

        return False