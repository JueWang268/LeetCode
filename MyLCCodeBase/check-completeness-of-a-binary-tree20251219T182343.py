from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # 1. left child > right child
        #2. # of nodes = 2^i
        q = deque()
        q.append(root)
        while q:
            n = q.popleft()
            # traverse the chilren
            # once its null the rest must be null
            if not n:
                for x in q:
                    if x is not None:
                        return False
                return True
            leftc = n.left
            rightc = n.right

            q.append(leftc)

            q.append(rightc)
            
        return True
                

