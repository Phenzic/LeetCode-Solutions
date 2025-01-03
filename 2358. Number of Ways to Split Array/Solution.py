class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        total_sum = sum(nums)
        left = 0

        for i in range(n-1):
            print(i)
            left += nums[i]
            right = total_sum - left
            if left >= right:
                ans += 1
        return ans