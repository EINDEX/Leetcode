# Combination Sum III

## Difficulty
Medium

## Question
<div>
<p>Find all possible combinations of <i><b>k</b></i> numbers that add up to a number <i><b>n</b></i>, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All numbers will be positive integers.</li>
	<li>The solution set must not contain duplicate combinations.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <i><b>k</b></i> = 3, <i><b>n</b></i> = 7
<strong>Output:</strong> [[1,2,4]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <i><b>k</b></i> = 3, <i><b>n</b></i> = 9
<strong>Output:</strong> [[1,2,6], [1,3,5], [2,3,4]]
</pre>
</div>

## Solution
### python
```python
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def inner(nums, k, n):
            if k == 0 and n == 0:
                res.append(nums)
            if len(nums) and n < nums[-1]:
                return
            if k == 0:
                return
            if not nums:
                m = 1
            else:
                m = nums[-1] + 1
            M = n // k+1
            if M > 10:
                M = 10
            for x in range(m, M):
                inner(nums+[x], k-1, n-x)
            
        inner([], k, n)
        return res
            
        

```
### python3
```python3
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def inner(nums, k, n):
            if k == 0 and n == 0:
                res.append(nums)
            if len(nums) and n < nums[-1]:
                return
            if k == 0:
                return
            if not nums:
                m = 1
            else:
                m = nums[-1] + 1
            M = n // k+1
            if M > 10:
                M = 10
            for x in range(m, M):
                inner(nums+[x], k-1, n-x)
            
        inner([], k, n)
        return res
            
        
```

## Author
EINDEX