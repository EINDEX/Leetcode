# Convert BST to Greater Tree

## Difficulty
Easy

## Question
<p>Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.</p>

<p>
<b>Example:</b>
<pre>
<b>Input:</b> The root of a Binary Search Tree like this:
              5
            /   \
           2     13

<b>Output:</b> The root of a Greater Tree like this:
             18
            /   \
          20     13
</pre>
</p>

## Solution
### python3
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        s = [0]
        def inner(node):
            if not node:
                return
            inner(node.right)
            node.val += s[0]
            s[0] = node.val
            inner(node.left)
            
        
        inner(root)
        return root
        
```

## Author
EINDEX