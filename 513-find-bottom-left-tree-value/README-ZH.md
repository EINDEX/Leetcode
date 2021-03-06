# Find Bottom Left Tree Value

## Difficulty
Medium

## Question
<p>
Given a binary tree, find the leftmost value in the last row of the tree. 
</p>

<p><b>Example 1:</b><br />
<pre>
Input:

    2
   / \
  1   3

Output:
1
</pre>
</p>

<p> <b> Example 2: </b><br>
<pre>
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
</pre>
</p>

<p><b>Note:</b>
You may assume the tree (i.e., the given root node) is not <b>NULL</b>.
</p>

## Solution
### python
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val
        

```

## Author
EINDEX