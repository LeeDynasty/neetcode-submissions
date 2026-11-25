# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        stack = [[root, 0]]
        retList = []
        while stack:
            node, level = stack.pop(0)

            if len(retList) < level+1:
                retList.insert(level, [node.val])
            else:
                retList[level].append(node.val)
            if node.left is not None:
                stack.append([node.left, level+1])
            if node.right is not None:
                stack.append([node.right, level+1])


        return retList
