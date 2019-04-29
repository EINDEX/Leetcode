# Power of Three

## Difficulty
Easy

## Question
<p>Given an integer, write a function to determine if it is a power of three.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input:</strong> 27
<strong>Output:</strong> true
</pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input:</strong> 0
<strong>Output:</strong> false</pre>

<p><b>Example 3:</b></p>

<pre>
<strong>Input:</strong> 9
<strong>Output:</strong> true</pre>

<p><b>Example 4:</b></p>

<pre>
<strong>Input:</strong> 45
<strong>Output:</strong> false</pre>

<p><b>Follow up:</b><br />
Could you do it without using any loop / recursion?</p>

## Solution
### python
```python
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        if n == 1:
            return True
        else:
            return False

```
### python3
```python3
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        if n == 1:
            return True
        else:
            return False
```

## Author
EINDEX