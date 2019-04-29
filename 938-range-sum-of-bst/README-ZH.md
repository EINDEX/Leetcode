# Range Sum of BST

## Difficulty
Easy

## Question
<p>Given the <code>root</code> node of a binary search tree, return the sum of values of all nodes with value between <code>L</code> and <code>R</code> (inclusive).</p>

<p>The binary search tree is guaranteed to have unique values.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-1-1">[10,5,15,3,7,null,18]</span>, L = <span id="example-input-1-2">7</span>, R = <span id="example-input-1-3">15</span>
<strong>Output: </strong><span id="example-output-1">32</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-2-1">[10,5,15,3,7,13,18,1,null,6]</span>, L = <span id="example-input-2-2">6</span>, R = <span id="example-input-2-3">10</span>
<strong>Output: </strong><span id="example-output-2">23</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>The number of nodes in the tree is at most <code>10000</code>.</li>
	<li>The final answer is guaranteed to be less than <code>2^31</code>.</li>
</ol>
</div>
</div>

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
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        if L <= root.val <= R:
            res = root.val
        else:
            res = 0
        res += self.rangeSumBST(root.left,L,R)
        res += self.rangeSumBST(root.right,L,R)
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
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        if L <= root.val <= R:
            res = root.val
        else:
            res = 0
        res += self.rangeSumBST(root.left,L,R)
        res += self.rangeSumBST(root.right,L,R)
        return res
        
            
            
        
```

## Author
EINDEX