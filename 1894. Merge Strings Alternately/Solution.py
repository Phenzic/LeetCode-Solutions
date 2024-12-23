class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        small = min(len(word1), len(word2))
        print(small)
        ans = ""
        for i in range(small):
            ans += word1[i]
            ans += word2[i]
        print(i)

        ban = (len(word1)>len(word2))
        print(ban)
        if ban == True:
            for i in range(small, len(word1)):
                ans += word1[i]
        elif ban == False:
            for i in range(small, len(word2)):
                print(i)
                ans += word2[i]
        return ans