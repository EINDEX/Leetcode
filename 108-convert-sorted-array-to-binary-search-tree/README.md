# Convert Sorted Array to Binary Search Tree

## Difficulty
Easy

## Question
<p>Given an array where elements are sorted in ascending order, convert it to a height balanced BST.</p>

<p>For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of <em>every</em> node never differ by more than 1.</p>

<p><strong>Example:</strong></p>

<pre>
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def inner(nums):
            if not nums:
                return None
            mid = len(nums)//2
            node = TreeNode(nums[mid])
            print(nums[:mid],nums[mid] ,nums[mid+1:])
            node.left = inner(nums[:mid])
            node.right = inner(nums[mid+1:])
            return node
        return inner(nums)
        

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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def inner(nums):
            if not nums:
                return None
            mid = len(nums)//2
            node = TreeNode(nums[mid])
            print(nums[:mid],nums[mid] ,nums[mid+1:])
            node.left = inner(nums[:mid])
            node.right = inner(nums[mid+1:])
            return node
        return inner(nums)
        
```

## Author
EINDEX