class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxi = 0
        stack = []
        for i, j in enumerate(heights):
            start = i
            while stack and stack[-1][1] > j:
                index, height = stack.pop()
                maxi = max(maxi, height * (i - index))
                start = index
            stack.append([start,j])
        print(stack, maxi)
        for i, h in stack:
            maxi = max(maxi, h*(len(heights)-i))
        return maxi

        