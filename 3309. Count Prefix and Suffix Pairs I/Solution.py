class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        def isPrefixAndSuffix(word1, word2):
            n, k = len(word1), len(word2)
            if n > k:
                return False
            if word2[:n] == word1 and  word2[(-1*n):] == word1:
                return True
            return False

        # words = sorted(words, key=len)
        print(words)
        i, j = 0, 1
        while i < len(words):
            print
            for l in range(j, len(words)):
                if isPrefixAndSuffix(words[i], words[l]):
                    print(words[i], words[l])
                    ans += 1

            i+=1
            j+=1
        return ans