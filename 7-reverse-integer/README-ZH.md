# Reverse Integer

## Difficulty
Easy

## Question
<p>Given a 32-bit signed integer, reverse digits of an integer.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 123
<strong>Output:</strong> 321
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> -123
<strong>Output:</strong> -321
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 120
<strong>Output:</strong> 21
</pre>

<p><strong>Note:</strong><br />
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.</p>


## Solution
### python
```python
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = -x
            res = -int(str(x)[::-1])
        else:
            res = int(str(x)[::-1])
        if res < - 2**31:
            return 0
        elif res > 2**31 -1:
            return 0
        else:
            return res
        


```
### python3
```python3
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = -x
            res = -int(str(x)[::-1])
        else:
            res = int(str(x)[::-1])
        if res < - 2**31:
            return 0
        elif res > 2**31 -1:
            return 0
        else:
            return res
        
```

## Author
EINDEX