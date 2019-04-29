# Combinations

## Difficulty
Medium

## Question
<p>Given two integers <em>n</em> and <em>k</em>, return all possible combinations of <em>k</em> numbers out of 1 ... <em>n</em>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;n = 4, k = 2
<strong>Output:</strong>
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
</pre>


## Solution
### python
```python
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def inner(nums, min_value, k):
            if k == 0:
                res.append(nums)
                return
            if min_value > n:
                return
            for x in range(min_value, n+1):
                inner(nums+[x], x+1,  k-1)
        
        inner([], 1, k)
        return res
        

```
### python3
```python3
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def inner(nums, min_value, k):
            if k == 0:
                res.append(nums)
                return
            if min_value > n:
                return
            for x in range(min_value, n+1):
                inner(nums+[x], x+1,  k-1)
        
        inner([], 1, k)
        return res
        
```

## Author
EINDEX