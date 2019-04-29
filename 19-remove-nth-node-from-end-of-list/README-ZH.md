# Remove Nth Node From End of List

## Difficulty
Medium

## Question
<p>Given a linked list, remove the <em>n</em>-th node from the end of list and return its head.</p>

<p><strong>Example:</strong></p>

<pre>
Given linked list: <strong>1-&gt;2-&gt;3-&gt;4-&gt;5</strong>, and <strong><em>n</em> = 2</strong>.

After removing the second node from the end, the linked list becomes <strong>1-&gt;2-&gt;3-&gt;5</strong>.
</pre>

<p><strong>Note:</strong></p>

<p>Given <em>n</em> will always be valid.</p>

<p><strong>Follow up:</strong></p>

<p>Could you do this in one pass?</p>


## Solution
### python
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        second = None
        first = head
        p = 0
        while first.next:
            first = first.next
            p += 1
            if p == n:
                second = head
            elif p > n:
                second = second.next
        if second:
            second.next = second.next.next
        elif head.next:
            head = head.next
        else:
            return None
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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        second = None
        first = head
        p = 0
        while first.next:
            first = first.next
            p += 1
            if p == n:
                second = head
            elif p > n:
                second = second.next
        if second:
            second.next = second.next.next
        elif head.next:
            head = head.next
        else:
            return None
        return head
        
        
```

## Author
EINDEX