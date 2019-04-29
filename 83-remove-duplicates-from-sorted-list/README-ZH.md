# Remove Duplicates from Sorted List

## Difficulty
Easy

## Question
<p>Given a sorted linked list, delete all duplicates such that each element appear only <em>once</em>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;1-&gt;2
<strong>Output:</strong> 1-&gt;2
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;1-&gt;2-&gt;3-&gt;3
<strong>Output:</strong> 1-&gt;2-&gt;3
</pre>


## Solution
### python
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head


```

## Author
EINDEX