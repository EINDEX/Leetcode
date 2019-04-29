# Binary Tree Level Order Traversal

## Difficulty
Medium

## Question
<p>Given a binary tree, return the <i>level order</i> traversal of its nodes' values. (ie, from left to right, level by level).</p>

<p>
For example:<br />
Given binary tree <code>[3,9,20,null,null,15,7]</code>,<br />
<pre>
    3
   / \
  9  20
    /  \
   15   7
</pre>
</p>
<p>
return its level order traversal as:<br />
<pre>
[
  [3],
  [9,20],
  [15,7]
]
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def inner(node, depth=1):
            if not node:
                return
            if len(res) < depth:
                res.append([])
            res[depth-1].append(node.val)
            inner(node.left,depth+1)
            inner(node.right,depth+1)
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def inner(node, depth=1):
            if not node:
                return
            if len(res) < depth:
                res.append([])
            res[depth-1].append(node.val)
            inner(node.left,depth+1)
            inner(node.right,depth+1)
        inner(root)
        return res
```

## Author
EINDEX