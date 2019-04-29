# Find Largest Value in Each Tree Row

## Difficulty
Medium

## Question
<p>You need to find the largest value in each row of a binary tree.</p>

<p><b>Example:</b><br />
<pre>
<b>Input:</b> 

          1
         / \
        3   2
       / \   \  
      5   3   9 

<b>Output:</b> [1, 3, 9]
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
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        def inner(node, depth=1):
            if not node:
                return
            if len(res) < depth:
                res.append(node.val)
            else:
                res[depth-1] = max(res[depth-1], node.val)
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
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        def inner(node, depth=1):
            if not node:
                return
            if len(res) < depth:
                res.append(node.val)
            else:
                res[depth-1] = max(res[depth-1], node.val)
            inner(node.left,depth+1)
            inner(node.right,depth+1)
        inner(root)
        return res
        
```

## Author
EINDEX