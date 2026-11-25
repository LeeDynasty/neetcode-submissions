# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        numList = []

        def dfs(node, parentVal):
            nonlocal numList
            if node is None:
                return
            
            dfs(node.left, node.val)
            numList.append(node.val)
            dfs(node.right, node.val)

        dfs(root, root.val)
        return numList[k-1]

