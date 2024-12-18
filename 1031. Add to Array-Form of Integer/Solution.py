class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number = 0
        ans = []
        s = ""
        for i in num:
            number = number * 10 + ord(str(i)) - ord("0")
        number = number + k
        while number > 0:
            s = (chr(ord('0') + number % 10)) + s 
            number //= 10
        print(s)
        for i in s:
            ans.append(int(i))
        return(ans)
