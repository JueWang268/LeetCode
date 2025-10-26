# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # ans = float("inf")
        def maxEndSum(node):
            # returns (max sum that starts with node, max path sum ever)
            # localmax = float("inf")
            if not node.left and not node.right:
                # localmax = max(localmax, node.val)
                return (node.val, node.val)
            l = r = (0,float("-inf"))
            if node.left:
                l = maxEndSum(node.left)
            if node.right:
                r = maxEndSum(node.right)
            mes = node.val + max(l[0],r[0],0)
            return (mes, max(l[1], r[1], node.val + max(0,l[0])+max(0,r[0])))
        return max(maxEndSum(root))
            



            



