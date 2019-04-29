# N-ary Tree Level Order Traversal

## Difficulty
Easy

## Question
<p>Given an n-ary tree, return the level order traversal of its nodes&#39; values. (ie, from left to right, level by level).</p>

<p>For example, given a <code>3-ary</code> tree:</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" /></p>

<p>&nbsp;</p>

<p>We should return its level order traversal:</p>

<pre>
[
     [1],
     [3,2,4],
     [5,6]
]
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The depth of the tree is at most <code>1000</code>.</li>
	<li>The total number of nodes is at most <code>5000</code>.</li>
</ol>


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
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        def inner(node, depth=0):
            if not node:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            if node.children:
                for c in node.children:
                    inner(c, depth+1)
        inner(root)
        return res
        
```

## Author
EINDEX