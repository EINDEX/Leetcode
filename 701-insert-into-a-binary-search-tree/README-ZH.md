# Insert into a Binary Search Tree

## Difficulty
Medium

## Question
<p>Given the root node of a binary search tree (BST) and a value to be inserted into the tree,&nbsp;insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.</p>

<p>Note that there may exist&nbsp;multiple valid ways for the&nbsp;insertion, as long as the tree remains a BST after insertion. You can return any of them.</p>

<p>For example,&nbsp;</p>

<pre>
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
</pre>

<p>You can return this binary search tree:</p>

<pre>
         4
       /   \
      2     7
     / \   /
    1   3 5
</pre>

<p>This tree is also valid:</p>

<pre>
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
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
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        tmp = root
        flag = False
        while not flag:
            if tmp.val < val:
                if tmp.right:
                    tmp = tmp.right
                else:
                    tmp.right = TreeNode(val)
                    flag = True
            else:
                if tmp.left:
                    tmp = tmp.left
                else:
                    tmp.left =  TreeNode(val)
                    flag = True
        return root
        

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
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        tmp = root
        flag = False
        while not flag:
            if tmp.val < val:
                if tmp.right:
                    tmp = tmp.right
                else:
                    tmp.right = TreeNode(val)
                    flag = True
            else:
                if tmp.left:
                    tmp = tmp.left
                else:
                    tmp.left =  TreeNode(val)
                    flag = True
        return root
        
```

## Author
EINDEX