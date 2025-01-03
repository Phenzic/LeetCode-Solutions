class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if nums == []:
            return -1
        total = sum(nums)
        n = len(nums)
        left = 0
        ans = 0
        for i in range(n):
            print(i)
            left = sum(nums[:i])
            if total - nums[i]-left == left:
                ans = i

                return i
        return -1
        