# Construct Binary Tree from Preorder and Inorder Traversal

## Difficulty
Medium

## Question
<p>Given preorder and inorder traversal of a tree, construct the binary tree.</p>

<p><strong>Note:</strong><br />
You may assume that duplicates do not exist in the tree.</p>

<p>For example, given</p>

<pre>
preorder =&nbsp;[3,9,20,15,7]
inorder = [9,3,15,20,7]</pre>

<p>Return the following binary tree:</p>

<pre>
    3
   / \
  9  20
    /  \
   15   7</pre>


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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        l = inorder.index(root.val)
        r = len(inorder) - l - 1
        if l:
            root.left = self.buildTree(preorder[1:1+l],inorder[:l])
        if r:
            root.right = self.buildTree(preorder[-r:],inorder[-r:])
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        l = inorder.index(root.val)
        r = len(inorder) - l - 1
        if l:
            root.left = self.buildTree(preorder[1:1+l],inorder[:l])
        if r:
            root.right = self.buildTree(preorder[1+l:],inorder[l+1:])
        return root
            
        
```

## Author
EINDEX