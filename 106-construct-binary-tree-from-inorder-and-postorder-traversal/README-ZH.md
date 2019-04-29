# Construct Binary Tree from Inorder and Postorder Traversal

## Difficulty
Medium

## Question
<p>Given inorder and postorder traversal of a tree, construct the binary tree.</p>

<p><strong>Note:</strong><br />
You may assume that duplicates do not exist in the tree.</p>

<p>For example, given</p>

<pre>
inorder =&nbsp;[9,3,15,20,7]
postorder = [9,15,7,20,3]</pre>

<p>Return the following binary tree:</p>

<pre>
    3
   / \
  9  20
    /  \
   15   7
</pre>


## Solution
### python
```python
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
        l = inorder.index(root.val)
        r = len(inorder) - l - 1
        if l:
            root.left = self.buildTree(inorder[:l], postorder[:l])
        if r:
            root.right = self.buildTree(inorder[l+1:], postorder[l:l+r])
        return root
            
        

```
### python3
```python3
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
        l = inorder.index(root.val)
        r = len(inorder) - l - 1
        if l:
            root.left = self.buildTree(inorder[:l], postorder[:l])
        if r:
            root.right = self.buildTree(inorder[l+1:], postorder[l:l+r])
        return root
            
        
```

## Author
EINDEX