# Binary Tree Tilt

## Difficulty
Easy

## Question
<p>Given a binary tree, return the tilt of the <b>whole tree</b>.</p>

<p>The tilt of a <b>tree node</b> is defined as the <b>absolute difference</b> between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.</p>

<p>The tilt of the <b>whole tree</b> is defined as the sum of all nodes' tilt.</p>

<p><b>Example:</b><br />
<pre>
<b>Input:</b> 
         1
       /   \
      2     3
<b>Output:</b> 1
<b>Explanation:</b> 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
</pre>
</p>

<p><b>Note:</b>
<ol>
<li>The sum of node values in any subtree won't exceed the range of 32-bit integer. </li>
<li>All the tilt values won't exceed the range of 32-bit integer.</li>
</ol>
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
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _inner(root):
            res = 0
            if not root:
                res += 0
                return 0, 0
            else:
                l, rl = _inner(root.left)
                r, rr = _inner(root.right)
                res += rl
                res += rr
                return root.val + l + r, abs(l-r) + res
        return _inner(root)[1]


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
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _inner(root):
            res = 0
            if not root:
                res += 0
                return 0, 0
            else:
                l, rl = _inner(root.left)
                r, rr = _inner(root.right)
                res += rl
                res += rr
                return root.val + l + r, abs(l-r) + res
        return _inner(root)[1]

```

## Author
EINDEX