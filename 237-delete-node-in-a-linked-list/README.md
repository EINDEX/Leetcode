# Delete Node in a Linked List

## Difficulty
Easy

## Question
<p>Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.</p>

<p>Given linked list --&nbsp;head =&nbsp;[4,5,1,9], which looks like following:</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2018/12/28/237_example.png" style="margin-top: 5px; margin-bottom: 5px; width: 300px; height: 49px;" /></p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> head = [4,5,1,9], node = 5
<strong>Output:</strong> [4,1,9]
<strong>Explanation: </strong>You are given the second node with value 5, the linked list should become 4 -&gt; 1 -&gt; 9 after calling your function.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [4,5,1,9], node = 1
<strong>Output:</strong> [4,5,9]
<strong>Explanation: </strong>You are given the third node with value 1, the linked list should become 4 -&gt; 5 -&gt; 9 after calling your function.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The linked list will have at least two elements.</li>
	<li>All of the nodes&#39; values will be unique.</li>
	<li>The given node&nbsp;will not be the tail and it will always be a valid node of the linked list.</li>
	<li>Do not return anything from your function.</li>
</ul>


## Solution
### python
```python
#
# [237] Delete Node in a Linked List
#
# https://leetcode-cn.com/problems/delete-node-in-a-linked-list/description/
#
# algorithms
# Easy (36.55%)
# Total Accepted:    1.9K
# Total Submissions: 5.2K
# Testcase Example:  '[0,1]\nnode at index 0 (node.val = 0)'
#
# 请编写一个函数，使其可以删除某个链表中给定的（非末尾的）节点，您将只被给予要求被删除的节点。
# 
# 比如：假设该链表为 1 -> 2 -> 3 -> 4  ，给定您的为该链表中值为 3 的第三个节点，那么在调用了您的函数之后，该链表则应变成 1 -> 2
# -> 4 。
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node.next:
            return
        
        node.val = node.next.val
        node.next = node.next.next

```

## Author
EINDEX