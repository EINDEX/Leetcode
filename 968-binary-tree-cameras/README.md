# Binary Tree Cameras

## Difficulty
Hard

## Question
<p>Given a binary tree, we install cameras on the nodes of the tree.&nbsp;</p>

<p>Each camera at&nbsp;a node can monitor <strong>its parent, itself, and its immediate children</strong>.</p>

<p>Calculate the minimum number of cameras needed to monitor all nodes of the tree.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png" style="width: 138px; height: 163px;" />
<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[0,0,null,0,0]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>One camera is enough to monitor all nodes if placed as shown.
</pre>

<div>
<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png" style="width: 139px; height: 312px;" />
<pre>
<strong>Input: </strong><span id="example-input-2-1">[0,0,null,0,null,0,null,null,0]</span>
<strong>Output: </strong><span id="example-output-2">2
<strong>Explanation:</strong> At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.</span>
</pre>

<p><br />
<strong>Note:</strong></p>

<ol>
	<li>The number of nodes in the given tree will be in the range&nbsp;<code>[1, 1000]</code>.</li>
	<li><strong>Every</strong> node has value 0.</li>
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
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def inner(root):
            if not root.left and not root.right:
                return 1
            a = inner(root.left) if root.left else 0
            b = inner(root.right) if root.right else 0
            if a == 1 or b == 1:
                res[0] += 1
                return 2
            if a == 2 or b == 2:
                return 0
            return 1
        if 1 == inner(root):
            res[0] += 1
        return res[0]
        

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
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def inner(root):
            if not root.left and not root.right:
                return 1
            a = inner(root.left) if root.left else 0
            b = inner(root.right) if root.right else 0
            if a == 1 or b == 1:
                res[0] += 1
                return 2
            if a == 2 or b == 2:
                return 0
            return 1
        if 1 == inner(root):
            res[0] += 1
        return res[0]
        
```

## Author
EINDEX