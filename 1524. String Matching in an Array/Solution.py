class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        hash = {i : len(j) for i, j in enumerate(words)}
        sortedHash = sorted(hash.items(), key=lambda x:x[1])
        new_arr, ans = [], []

        print(hash, sortedHash)
        for i in sortedHash:
            p, q = i
            new_arr.append(words[p])
        print(new_arr)
        k = 0
        while k < len(words):
            for l in range(k+1, len(words)):
                print(new_arr[k], l)
                if ((new_arr[k] in new_arr[l]) and (new_arr[k] not in ans)):
                    print("yes")
                    ans.append(new_arr[k])
            k+=1
        return ans
        





