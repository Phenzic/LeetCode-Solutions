class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # convert int to binary and remove prefix '0b'
        a = bin(a)[2:]
        b = bin(b)[2:]
        c = bin(c)[2:]

        # to find maximum length of the binary strings
        max_len = max(len(a), len(b), len(c))

        # pad the binary strings with 0 to be same length
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        c = c.zfill(max_len)
        
        count = 0 # to keep track of no.of bits to be shifted

        for i in range(max_len): # to check each bit
            if c[i] == '0': 
            # if c[i]=0, then a[i] and b[i] should be 0
                count += int(a[i]) + int(b[i])
            elif a[i] == '0' and b[i] == '0': 
            # if c[i]=1, then either a[i] or b[i] should be 1
                    count += 1
       
        return count