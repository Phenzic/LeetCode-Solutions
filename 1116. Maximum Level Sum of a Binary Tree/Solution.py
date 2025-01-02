# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # def bfs(node):
        # queue = [source]
        queue = deque([root])
        max_sum = float("-inf")
        max_level = 0
        curr_level = 1
        while queue:
            level_size = len(queue)
            level_sum = 0
            for i in range(level_size):
                curr = queue.popleft()
                level_sum += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = curr_level
            curr_level +=1

        return max_level