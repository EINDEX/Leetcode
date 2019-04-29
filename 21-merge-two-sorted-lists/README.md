# Merge Two Sorted Lists

## Difficulty
Easy

## Question
<p>Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.</p>

<p><b>Example:</b>
<pre>
<b>Input:</b> 1->2->4, 1->3->4
<b>Output:</b> 1->1->2->3->4->4
</pre>
</p>

## Solution
### python
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1
        head = l1    
        while l2:
            if not l1.next:
                l1.next = l2
                break
            if l1.next.val > l2.val:
                tmp = l2.next
                l2.next = l1.next
                l1.next = l2
                l2 = tmp
            t = head
            l1 = l1.next 
                        
        return head

```
### python3
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1
        head = l1    
        while l2:
            if not l1.next:
                l1.next = l2
                break
            if l1.next.val > l2.val:
                tmp = l2.next
                l2.next = l1.next
                l1.next = l2
                l2 = tmp
            t = head
            l1 = l1.next 
                        
        return head
```

## Author
EINDEX