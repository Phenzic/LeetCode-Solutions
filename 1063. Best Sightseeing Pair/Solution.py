class Solution(object):
    def maxScoreSightseeingPair(self, values):
        max_score = 0
        max_i = values[0]
        
        for j in range(1, len(values)):
            max_score = max(max_score, max_i + values[j] - j)

            max_i = max(max_i, values[j] + j)
        
        return max_score

        # high = 0
        # i, j = 0, len(values) - 1
        # while i < j:
        #     high = max (values[i] + values[j] + (i - j), high)
        #     print(values[i], values[j])
        #     if values[i] < values[j]:
        #         i+= 1
        #     else:
        #         j -= 1
        
        # return high
        