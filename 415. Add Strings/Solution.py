class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num_1, num_2 = 0, 0
        for i in num1:
            num_1 = num_1 * 10 + ord(i) - ord("0")
        for j in num2:
            num_2 = num_2 * 10 + ord(j) - ord("0")
        num3 = num_1 + num_2
        if num3 == 0:
            return "0"
        st = ""
        while num3 > 0:
            n = num3 % 10
            n = chr(n + 48)
            st = n + st
            num3 //= 10
        return st
