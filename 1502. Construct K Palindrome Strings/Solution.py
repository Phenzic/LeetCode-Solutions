class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        # hash = {}
        chars = Counter(s)
        print(chars)

        count = 0
    
        for _, value in chars.items(): 
            if value % 2 != 0:  
                count += 1
            if count > k:  
                return False
        return count <= k