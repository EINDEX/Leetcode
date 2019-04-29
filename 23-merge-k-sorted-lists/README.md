# Merge k Sorted Lists

## Difficulty
Hard

## Question
<p>Merge <em>k</em> sorted linked lists and return it as one sorted list. Analyze and describe its complexity.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>
[
&nbsp; 1-&gt;4-&gt;5,
&nbsp; 1-&gt;3-&gt;4,
&nbsp; 2-&gt;6
]
<strong>Output:</strong> 1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
</pre>


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
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        t = lists[0]
        for i in range(1, len(lists)):
            t = self.mergeTwoLists(t, lists[i])
        return t
        
        

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
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        t = lists[0]
        for i in range(1, len(lists)):
            t = self.mergeTwoLists(t, lists[i])
        return t
        
        
```

## Author
EINDEX