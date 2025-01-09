class Solution:
    def tribonacci(self, n: int) -> int:
        keep = [0, 1, 1]
        p = len(keep)
        if n <= p-1:
            return keep[n]
        for i in range(p, n+1):
            keep.append(sum(keep[-3:]))
        return keep[-1]

