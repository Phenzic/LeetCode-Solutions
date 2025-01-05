class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Pair nums2 and nums1, and sort by nums2 in descending order
        merged = sorted(zip(nums2, nums1), reverse=True)
        
        score = float("-inf")  # Initialize max score
        heap = []  # Min-heap to store top k elements from nums1
        current_sum = 0  # Sum of elements in the heap
        
        # Iterate over the sorted pairs
        for num2, num1 in merged:
            # If heap exceeds size k, remove the smallest element
            if len(heap) == k:
                current_sum -= heapq.heappop(heap)
            
            # Add the current num1 to the heap and update the sum
            heapq.heappush(heap, num1)
            current_sum += num1
            
            # If the heap contains exactly k elements, calculate the score
            if len(heap) == k:
                score = max(score, current_sum * num2)
        
        return score