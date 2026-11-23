# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        node_queue = [root]

        while len(node_queue) > 0:
            currNode = node_queue.pop(0)
            leftNode = currNode.left
            rightNode = currNode.right
            if (leftNode is not None):
                node_queue.append(leftNode)
            if (rightNode is not None):
                node_queue.append(rightNode)
            
            currNode.left = rightNode
            currNode.right = leftNode

        return root