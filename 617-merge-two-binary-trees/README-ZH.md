# Merge Two Binary Trees

## Difficulty
Easy

## Question
<p>Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.</p>

<p>You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
<b>Output:</b> 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
</pre>

<p>&nbsp;</p>

<p><b>Note:</b> The merging process must start from the root nodes of both trees.</p>


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
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val += t2.val
        elif t2:
            return t2
        else:
            return t1
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)
        return t1
        
```

## Author
EINDEX