# Leaf-Similar Trees

## Difficulty
Easy

## Question
<p>Consider all the leaves of a binary tree.&nbsp; From&nbsp;left to right order, the values of those&nbsp;leaves form a <em>leaf value sequence.</em></p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png" style="width: 300px; height: 240px;" /></p>

<p>For example, in the given tree above, the leaf value sequence is <code>(6, 7, 4, 9, 8)</code>.</p>

<p>Two binary trees are considered <em>leaf-similar</em>&nbsp;if their leaf value sequence is the same.</p>

<p>Return <code>true</code> if and only if the two given trees with head nodes <code>root1</code> and <code>root2</code> are leaf-similar.</p>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Both of the given trees will have between <code>1</code> and <code>100</code> nodes.</li>
</ul>


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
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaf_list(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return get_leaf_list(node.left) + get_leaf_list(node.right)
        return get_leaf_list(root1) == get_leaf_list(root2)

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
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaf_list(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return get_leaf_list(node.left) + get_leaf_list(node.right)
        return get_leaf_list(root1) == get_leaf_list(root2)
```

## Author
EINDEX