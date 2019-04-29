# Power of Two

## Difficulty
Easy

## Question
<p>Given an integer, write a function to determine if it is a power of two.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 1
<strong>Output:</strong> true 
<strong>Explanation: </strong>2<sup>0</sup>&nbsp;= 1
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 16
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>4</sup>&nbsp;= 16</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 218
<strong>Output:</strong> false</pre>


## Solution
### python
```python
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & (n - 1))

```
### python3
```python3
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & (n - 1))
```

## Author
EINDEX