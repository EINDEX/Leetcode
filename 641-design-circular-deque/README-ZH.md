# Design Circular Deque

## Difficulty
Medium

## Question
<p>Design your implementation of the circular double-ended queue (deque).</p>

<p>Your implementation should support following operations:</p>

<ul>
	<li><code>MyCircularDeque(k)</code>: Constructor, set the size of the deque to be k.</li>
	<li><code>insertFront()</code>: Adds an item at the front of Deque. Return true if the operation is successful.</li>
	<li><code>insertLast()</code>: Adds an item at the rear of Deque. Return true if the operation is successful.</li>
	<li><code>deleteFront()</code>: Deletes an item from the front of Deque. Return true if the operation is successful.</li>
	<li><code>deleteLast()</code>: Deletes an item from the rear of Deque. Return true if the operation is successful.</li>
	<li><code>getFront()</code>: Gets the front item from the Deque. If the deque is empty, return -1.</li>
	<li><code>getRear()</code>: Gets the last item from Deque. If the deque is empty, return -1.</li>
	<li><code>isEmpty()</code>: Checks whether Deque is empty or not.&nbsp;</li>
	<li><code>isFull()</code>: Checks whether Deque is full or not.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All values will be in the range of [0, 1000].</li>
	<li>The number of operations will be in the range of&nbsp;[1, 1000].</li>
	<li>Please do not use the built-in Deque library.</li>
</ul>


## Solution
### python3
```python3
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.max = k
        self.k = []
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.k = [value] + self.k 
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.k = self.k + [value] 
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.k.pop(0)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.k.pop(-1)
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.k[0]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.k[-1]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.k:
            return False
        return True
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.k) == self.max


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```

## Author
EINDEX