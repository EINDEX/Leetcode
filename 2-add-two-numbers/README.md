# Add Two Numbers

## Difficulty
Medium

## Question
<p>You are given two <b>non-empty</b> linked lists representing two non-negative integers. The digits are stored in <b>reverse order</b> and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> (2 -&gt; 4 -&gt; 3) + (5 -&gt; 6 -&gt; 4)
<b>Output:</b> 7 -&gt; 0 -&gt; 8
<b>Explanation:</b> 342 + 465 = 807.
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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        p = None
        flag = 0
        while l1 and l2:
            t = l1.val + l2.val + flag
            if not p:
                p = ListNode(t%10)
            else:
                p.next = ListNode(t%10)
                p = p.next
            if not head:
                head = p
            flag = t // 10
            l1 = l1.next
            l2 = l2.next
        if l1 or l2 or flag:
            if l1:
                p.next = l1
            elif l2:
                p.next = l2
            else:
                p.next = None
            
            while p.next or flag:
                if  p.next:
                    t =  p.next.val + flag
                    p.next.val = t % 10
                else:
                    t = flag
                    p.next = ListNode(t%10)
                flag = t // 10
                p =  p.next
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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        p = None
        flag = 0
        while l1 and l2:
            t = l1.val + l2.val + flag
            if not p:
                p = ListNode(t%10)
            else:
                p.next = ListNode(t%10)
                p = p.next
            if not head:
                head = p
            flag = t // 10
            l1 = l1.next
            l2 = l2.next
        if l1 or l2 or flag:
            if l1:
                p.next = l1
            elif l2:
                p.next = l2
            else:
                p.next = None
            
            while p.next or flag:
                if  p.next:
                    t =  p.next.val + flag
                    p.next.val = t % 10
                else:
                    t = flag
                    p.next = ListNode(t%10)
                flag = t // 10
                p =  p.next
        return head
```

## Author
EINDEX