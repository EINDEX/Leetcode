# N-ary Tree Preorder Traversal

## Difficulty
Easy

## Question
<p>Given an n-ary tree, return the <i>preorder</i> traversal of its nodes&#39; values.</p>

<p>For example, given a <code>3-ary</code> tree:</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" /></p>

<p>&nbsp;</p>

<p>Return its preorder traversal as: <code>[1,3,5,6,2,4]</code>.</p>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<p>Recursive solution is trivial, could you do it iteratively?</p>


## Solution
### python
```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        res.append(root.val)
        if root.children:
            for c in root.children:
                res += self.preorder(c)      
        return res

```

## Author
EINDEX