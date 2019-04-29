# Palindrome Linked List

## Difficulty
Easy

## Question
<p>Given a singly linked list, determine if it is a palindrome.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2
<strong>Output:</strong> false</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 1-&gt;2-&gt;2-&gt;1
<strong>Output:</strong> true</pre>

<p><b>Follow up:</b><br />
Could you do it in O(n) time and O(1) space?</p>


## Solution
### python
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        if res == res[::-1]:
            return True
        return False

```
### python3
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        if res == res[::-1]:
            return True
        return False
```

## Author
EINDEX