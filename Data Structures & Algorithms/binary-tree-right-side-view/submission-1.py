# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        retList = []
        stack = [[root, 0]]
        
        while stack:
            node, depth = stack.pop(0)
            if len(retList) < depth+1:
                retList.append(node.val)

            if node.right:
                stack.append([node.right, depth + 1])
            if node.left:
                stack.append([node.left, depth + 1])
        
        return retList
