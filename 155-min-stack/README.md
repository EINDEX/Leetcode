# Min Stack

## Difficulty
Easy

## Question
<p>
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
<ul>
<li>
push(x) -- Push element x onto stack.
</li>
<li>
pop() -- Removes the element on top of the stack.
</li>
<li>
top() -- Get the top element.
</li>
<li>
getMin() -- Retrieve the minimum element in the stack.
</li>
</ul>
</p>

<p><b>Example:</b><br />
<pre>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
</pre>
</p>

## Solution
### python
```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stash = []
        self.min_helper = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stash.append(x)
        if not self.min_helper:
            self.min_helper.append(len(self.stash) - 1)
        elif x < self.getMin():
            self.min_helper.append(len(self.stash) - 1)
        

    def pop(self):
        """
        :rtype: void
        """
        self.stash.pop()
        if self.min_helper[-1] == len(self.stash):
            self.min_helper.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stash[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stash[self.min_helper[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

```
### python3
```python3
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stash = []
        self.min_helper = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stash.append(x)
        if not self.min_helper:
            self.min_helper.append(len(self.stash) - 1)
        elif x < self.getMin():
            self.min_helper.append(len(self.stash) - 1)
        

    def pop(self):
        """
        :rtype: void
        """
        self.stash.pop()
        if self.min_helper[-1] == len(self.stash):
            self.min_helper.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stash[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stash[self.min_helper[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

## Author
EINDEX