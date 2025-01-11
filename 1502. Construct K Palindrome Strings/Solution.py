class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        # hash = {}
        chars = Counter(s)
        print(chars)

        count = 0
    
        for _, value in chars.items():  # Iterate over key-value pairs
            if value % 2 != 0:  # Check if the value is odd
                count += 1
            if count > k:  # Return False if count exceeds k
                return False
        
        return count <= k  


        

    #     let count = 0;
    #     for (let v of Object.entries(map)) {
    #         if (v[1] % 2 !== 0) {
    #             count++
    #         }
    #         if (count > k) return false;
    #     }

    #     return count <= k;
    # };
    # ```
            