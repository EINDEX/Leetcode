# Factorial Trailing Zeroes

## Difficulty
Easy

## Question
<p>Given an integer <i>n</i>, return the number of trailing zeroes in <i>n</i>!.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 3
<strong>Output:</strong> 0
<strong>Explanation:</strong>&nbsp;3! = 6, no trailing zero.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 5
<strong>Output:</strong> 1
<strong>Explanation:</strong>&nbsp;5! = 120, one trailing zero.</pre>

<p><b>Note: </b>Your solution should be in logarithmic time complexity.</p>


## Solution
### python
```python
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        res = 0
        while True:
            k = n // (5 ** count)
            if k == 0:
                break
            res += k
            count += 1
        return res



```
### python3
```python3
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        res = 0
        while True:
            k = n // (5 ** count)
            if k == 0:
                break
            res += k
            count += 1
        return res

```

## Author
EINDEX