class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        maxi = 0 
        right, left = 0, 0
        for i in range(1,n):
            p = s[0:i]
            q = s[i:]
            print(p.count("0"))
            print(q.count("1"))
            maxi = max(maxi, (p.count("0") + q.count("1")))

        return maxi

        