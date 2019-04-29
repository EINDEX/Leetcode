# Permutations

## Difficulty
Medium

## Question
<p>Given a collection of <strong>distinct</strong> integers, return all possible permutations.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3]
<strong>Output:</strong>
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
</pre>


## Solution
### python
```python
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 每次从已有数字中选取一个数字然后进入下一次迭代
        res = []
        def inner(num, nums):
            for n in nums:
                inner(num+[n], [i for i in nums if i !=n])
            if not nums:
                res.append(num)
        
        inner([], nums)
        return res

```
### python3
```python3
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 每次从已有数字中选取一个数字然后进入下一次迭代
        res = []
        def inner(num, nums):
            for n in nums:
                inner(num+[n], [i for i in nums if i !=n])
            if not nums:
                res.append(num)
        
        inner([], nums)
        return res
```

## Author
EINDEX