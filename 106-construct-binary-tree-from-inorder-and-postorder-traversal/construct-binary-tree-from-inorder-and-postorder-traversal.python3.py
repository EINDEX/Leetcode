# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        l = i - 0
        r = len(inorder) - i - 1
        left_i = inorder[:l]
        left_p = postorder[:l]
        root.left = self.buildTree(left_i, left_p)
        right_i = inorder[l+1:]
        right_p = postorder[l:l+r]
        root.right = self.buildTree(right_i, right_p)
        return root
            
        