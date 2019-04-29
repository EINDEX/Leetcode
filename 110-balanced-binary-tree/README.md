# Balanced Binary Tree

## Difficulty
Easy

## Question
<p>Given a binary tree, determine if it is height-balanced.</p>

<p>For this problem, a height-balanced binary tree is defined as:</p>

<blockquote>
<p>a binary tree in which the depth of the two subtrees of <em>every</em> node never differ by more than 1.</p>
</blockquote>

<p><strong>Example 1:</strong></p>

<p>Given the following tree <code>[3,9,20,null,null,15,7]</code>:</p>

<pre>
    3
   / \
  9  20
    /  \
   15   7</pre>

<p>Return true.<br />
<br />
<strong>Example 2:</strong></p>

<p>Given the following tree <code>[1,2,2,3,3,null,null,4,4]</code>:</p>

<pre>
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
</pre>

<p>Return false.</p>


## Solution
### python3
```python3
#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (45.94%)
# Total Accepted:    9.5K
# Total Submissions: 20.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 
# 本题中，一棵高度平衡二叉树定义为：
# 
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
# 
# 
# 示例 1:
# 
# 给定二叉树 [3,9,20,null,null,15,7]
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回 true 。
# 
# 示例 2:
# 
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# 返回 false 。
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inner(node):
            if not node:
                return 0
            l = inner(node.left) + 1
            r = inner(node.right) + 1
            if abs(l - r) > 1:
                return 999
            else:
                return max(l, r)
        if inner(root) >= 999:
            return False
        return True
        

```

## Author
EINDEX