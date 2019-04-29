# Sum of Left Leaves

## Difficulty
Easy

## Question
<p>Find the sum of all left leaves in a given binary tree.</p>

<p><b>Example:</b>
<pre>
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values <b>9</b> and <b>15</b> respectively. Return <b>24</b>.
</pre>
</p>

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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _inner(root, is_left):
            if not root:
                return 0
            if is_left and not root.left and not root.right:
                return root.val
            x = 0
            return x + _inner(root.left, True) + _inner(root.right, False)
        return _inner(root, False)



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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _inner(root, is_left):
            if not root:
                return 0
            if is_left and not root.left and not root.right:
                return root.val
            x = 0
            return x + _inner(root.left, True) + _inner(root.right, False)
        return _inner(root, False)

```

## Author
EINDEX