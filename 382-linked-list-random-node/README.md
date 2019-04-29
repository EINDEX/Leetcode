# Linked List Random Node

## Difficulty
Medium

## Question
<p>Given a singly linked list, return a random node's value from the linked list. Each node must have the <b>same probability</b> of being chosen.</p>

<p><b>Follow up:</b><br />
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?
</p>

<p><b>Example:</b>
<pre>
// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
</pre>
</p>

## Solution
### python
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        choose = None
        this = self.head
        max_val = 0
        while this is not None:
            val = random.random()
            if val > max_val:
                max_val = val
                choose = this
            this= this.next
        return choose.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

## Author
EINDEX