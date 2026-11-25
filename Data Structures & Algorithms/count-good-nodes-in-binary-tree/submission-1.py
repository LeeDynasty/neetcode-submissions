# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        numGoodNodes = 0

        def dfs(node, currVal):
            nonlocal numGoodNodes

            if node is None:
                return
            elif node.val >= currVal:

                numGoodNodes += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            else:
                dfs(node.left, currVal)
                dfs(node.right, currVal)
        
        dfs(root, root.val)

        return numGoodNodes


            