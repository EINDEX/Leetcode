# Missing Number

## Difficulty
Easy

## Question
<p>Given an array containing <i>n</i> distinct numbers taken from <code>0, 1, 2, ..., n</code>, find the one that is missing from the array.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [3,0,1]
<b>Output:</b> 2
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [9,6,4,2,3,5,7,0,1]
<b>Output:</b> 8
</pre>

<p><b>Note</b>:<br />
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?</p>

## Solution
### python
```python
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        b = 0
        for x in range(l+1):
            b ^= x
        for x in nums:
            b  ^= x
        return b

```
### python3
```python3
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = ((len(nums) + 0) * (len(nums)+1)//2)
        return s - sum(nums)

```

## Author
EINDEX