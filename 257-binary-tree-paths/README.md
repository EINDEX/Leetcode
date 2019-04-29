# Binary Tree Paths

## Difficulty
Easy

## Question
<p>Given a binary tree, return all root-to-leaf paths.</p>

<p><strong>Note:</strong>&nbsp;A leaf is a node with no children.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>

   1
 /   \
2     3
 \
  5

<strong>Output:</strong> [&quot;1-&gt;2-&gt;5&quot;, &quot;1-&gt;3&quot;]

<strong>Explanation:</strong> All root-to-leaf paths are: 1-&gt;2-&gt;5, 1-&gt;3
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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def inner(path, node):
            if not node:
                return
            path = path[:]
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append(path)
            inner(path, node.left)
            inner(path, node.right)
        inner([], root)
        return ['->'.join(p) for p in res]
        

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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def inner(path, node):
            if not node:
                return
            path = path[:]
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append(path)
            inner(path, node.left)
            inner(path, node.right)
        inner([], root)
        return ['->'.join(p) for p in res]
        
```

## Author
EINDEX