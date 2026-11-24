# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack = [p]
        q_stack = [q]

        while p_stack and q_stack:
            p_node = p_stack.pop(-1)
            q_node = q_stack.pop(-1)

            if p_node is None and q_node is None:
                continue
            elif p_node is None or q_node is None:
                return False
            else:
                if p_node.val != q_node.val:
                    return False
            
            p_stack.append(p_node.left)
            p_stack.append(p_node.right)
            q_stack.append(q_node.left)
            q_stack.append(q_node.right)

        if len(p_stack) != len(q_stack):
            return False
        
        return True