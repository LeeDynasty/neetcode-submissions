# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            else:
                if node1.val != node2.val:
                    return False
            
            return sameTree(node1.left, node2.left) and sameTree(node1.right, node2.right)

        rootstack = [root]

        while rootstack:
            node = rootstack.pop(0)
            if node.val == subRoot.val and sameTree(node, subRoot):
                return True
            if node.left:
                rootstack.append(node.left)
            if node.right:
                rootstack.append(node.right)

        return False

