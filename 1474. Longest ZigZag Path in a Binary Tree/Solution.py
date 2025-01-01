# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curLen, goLeft):
            if not node:
                return curLen 
            
            if goLeft:
                return max(dfs(node.left, curLen + 1, False), dfs(node.right, 0, True))
            else:
                return max(dfs(node.left, 0, False), dfs(node.right, curLen + 1, True))

        return max(dfs(root.left, 0, False), dfs(root.right, 0, True))

        