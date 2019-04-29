# Swap Nodes in Pairs

## Difficulty
Medium

## Question
<p>Given a&nbsp;linked list, swap every two adjacent nodes and return its head.</p>

<p>You may <strong>not</strong> modify the values in the list&#39;s nodes, only nodes itself may be changed.</p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
Given <code>1-&gt;2-&gt;3-&gt;4</code>, you should return the list as <code>2-&gt;1-&gt;4-&gt;3</code>.
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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            t = self.swapPairs(head.next.next)
        else:
            return head
        # print(t.val)
        a = head
        b = head.next
        b.next = a
        a.next = t
        return b

```
### python3
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            t = self.swapPairs(head.next.next)
        else:
            return head
        # print(t.val)
        a = head
        b = head.next
        b.next = a
        a.next = t
        return b
```

## Author
EINDEX