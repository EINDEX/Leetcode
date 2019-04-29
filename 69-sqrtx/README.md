# Sqrt(x)

## Difficulty
Easy

## Question
<p>Implement <code>int sqrt(int x)</code>.</p>

<p>Compute and return the square root of <em>x</em>, where&nbsp;<em>x</em>&nbsp;is guaranteed to be a non-negative integer.</p>

<p>Since the return type&nbsp;is an integer, the decimal digits are truncated and only the integer part of the result&nbsp;is returned.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 4
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 8
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 8 is 2.82842..., and since 
&nbsp;            the decimal part is truncated, 2 is returned.
</pre>


## Solution
### python
```python
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        l = 0
        h = x // 2 + 1
        mid = 0

        while(l <= h):
            mid = (l+h) // 2
            if mid ** 2 > x:
                h = mid - 1
            elif mid ** 2 < x:
                l = mid + 1
            else:
                return mid
        return (l+h) // 2




```
### python3
```python3
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        l = 0
        h = x // 2 + 1
        mid = 0

        while(l <= h):
            mid = (l+h) // 2
            if mid ** 2 > x:
                h = mid - 1
            elif mid ** 2 < x:
                l = mid + 1
            else:
                return mid
        return (l+h) // 2


```

## Author
EINDEX