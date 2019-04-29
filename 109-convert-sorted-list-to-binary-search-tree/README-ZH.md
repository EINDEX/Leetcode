# Convert Sorted List to Binary Search Tree

## Difficulty
Medium

## Question
<p>Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.</p>

<p>For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of <em>every</em> node never differ by more than 1.</p>

<p><strong>Example:</strong></p>

<pre>
Given the sorted linked list: [-10,-3,0,5,9],

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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        a, b, c= head, head, None
        while b.next:
            c = a
            a = a.next
            if b.next.next:
                b = b.next.next
            else:
                b = b.next
                break
        if c:
            c.next = None
        node = TreeNode(a.val)
        node.right = self.sortedListToBST(a.next)
        node.left = self.sortedListToBST(head)
        return node
                
            
            
        

```
### python3
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        a, b, c= head, head, None
        while b.next:
            c = a
            a = a.next
            if b.next.next:
                b = b.next.next
            else:
                b = b.next
                break
        if c:
            c.next = None
        node = TreeNode(a.val)
        node.right = self.sortedListToBST(a.next)
        node.left = self.sortedListToBST(head)
        return node
                
            
            
        
```

## Author
EINDEX