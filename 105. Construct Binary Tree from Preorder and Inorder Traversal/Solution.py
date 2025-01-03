# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        graph = {}
    
        for i in range(len(inorder)):
            graph[inorder[i]] = i
        preorder = deque(preorder)
        print(preorder, graph)

        def dfs(start, end):
            if start > end: return None
            root = TreeNode(preorder.popleft())
            mid = graph[root.val]

            root.left = dfs(start, mid -1)
            root.right = dfs(mid + 1, end)

            return root

        return dfs(0, len(preorder) - 1)
