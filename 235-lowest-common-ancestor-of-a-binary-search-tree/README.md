# Lowest Common Ancestor of a Binary Search Tree

## Difficulty
Easy

## Question
<p>Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.</p>

<p>According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: &ldquo;The lowest common ancestor is defined between two nodes p and q&nbsp;as the lowest node in T that has both p and q&nbsp;as descendants (where we allow <b>a node to be a descendant of itself</b>).&rdquo;</p>

<p>Given binary search tree:&nbsp; root =&nbsp;[6,2,8,0,4,7,9,null,null,3,5]</p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 200px; height: 190px;" />
<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
<strong>Output:</strong> 6
<strong>Explanation: </strong>The LCA of nodes <code>2</code> and <code>8</code> is <code>6</code>.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
<strong>Output:</strong> 2
<strong>Explanation: </strong>The LCA of nodes <code>2</code> and <code>4</code> is <code>2</code>, since a node can be a descendant of itself according to the LCA definition.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All of the nodes&#39; values will be unique.</li>
	<li>p and q are different and both values will&nbsp;exist in the BST.</li>
</ul>


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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def get_path(path, node, target):
            path.append(node)
            if node.val == target.val:
                return path
            elif node.val > target.val:
                return get_path(path, node.left, target)
            else:
                return get_path(path, node.right, target)
        
        p1 = get_path([], root, p)
        p2 = get_path([], root, q)
        x = 0
        while len(p1) > x and len(p2) > x:
            if p1[x].val != p2[x].val:
                break
            x += 1
        return p1[x-1]
            

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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def get_path(path, node, target):
            path.append(node)
            if node.val == target.val:
                return path
            elif node.val > target.val:
                return get_path(path, node.left, target)
            else:
                return get_path(path, node.right, target)
        
        p1 = get_path([], root, p)
        p2 = get_path([], root, q)
        x = 0
        while len(p1) > x and len(p2) > x:
            if p1[x].val != p2[x].val:
                break
            x += 1
        return p1[x-1]
            
```

## Author
EINDEX