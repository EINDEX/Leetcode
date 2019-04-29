# Symmetric Tree

## Difficulty
Easy

## Question
<p>Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).</p>

<p>
For example, this binary tree <code>[1,2,2,3,4,4,3]</code> is symmetric:
<pre>
    1
   / \
  2   2
 / \ / \
3  4 4  3
</pre>
</p>
<p>
But the following <code>[1,2,2,null,3,null,3]</code>  is not:<br />
<pre>
    1
   / \
  2   2
   \   \
   3    3
</pre>
</p>

<p>
<b>Note:</b><br />
Bonus points if you could solve it both recursively and iteratively.
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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def inner(l,r):
            if l and r and l.val == r.val:
                return inner(l.right,r.left) and inner(l.left, r.right)
            elif not l and not r:
                return True
            else:
                return False
      
        return inner(root.left, root.right)

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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def inner(l,r):
            if l and r and l.val == r.val:
                return inner(l.right,r.left) and inner(l.left, r.right)
            elif not l and not r:
                return True
            else:
                return False
      
        return inner(root.left, root.right)
```

## Author
EINDEX