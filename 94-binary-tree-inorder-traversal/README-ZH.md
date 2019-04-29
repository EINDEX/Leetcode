# Binary Tree Inorder Traversal

## Difficulty
Medium

## Question
<p>Given a binary tree, return the <em>inorder</em> traversal of its nodes&#39; values.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,null,2,3]
   1
    \
     2
    /
   3

<strong>Output:</strong> [1,3,2]</pre>

<p><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>


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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def inner(node):
            if node:
                inner(node.left)
                res.append(node.val)
                inner(node.right)
        inner(root)
        return res

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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def inner(node):
            if node:
                inner(node.left)
                res.append(node.val)
                inner(node.right)
        inner(root)
        return res
```

## Author
EINDEX