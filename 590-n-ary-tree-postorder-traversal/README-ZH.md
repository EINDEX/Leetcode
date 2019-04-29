# N-ary Tree Postorder Traversal

## Difficulty
Easy

## Question
<p>Given an n-ary tree, return the <i>postorder</i> traversal of its nodes&#39; values.</p>

<p>For example, given a <code>3-ary</code> tree:</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" /></p>

<p>&nbsp;</p>

<p>Return its postorder traversal as: <code>[5,6,3,2,4,1]</code>.</p>
&nbsp;

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
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        if root.children:
            for c in root.children:
                res += self.postorder(c)
        res+=[root.val]
        return res
```

## Author
EINDEX