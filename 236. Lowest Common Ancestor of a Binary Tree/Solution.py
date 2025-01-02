# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if not node:
                return None
            if node == p or node == q:
                print(node)
                return node
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                print(node)
                return node
                
            print(left, right)
            return left if left else right

        return dfs(root)
        # curr = root
        # while curr:
        #     if p.val > curr.val and q.val > curr.val:
        #         curr = curr.right
        #     elif p.val < curr.val and q.val < curr.val:
        #         curr = curr.left
        #     else: 
        #         return curr

        