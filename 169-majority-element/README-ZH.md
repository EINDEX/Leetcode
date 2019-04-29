# Majority Element

## Difficulty
Easy

## Question
<p>Given an array of size <i>n</i>, find the majority element. The majority element is the element that appears <b>more than</b> <code>&lfloor; n/2 &rfloor;</code> times.</p>

<p>You may assume that the array is non-empty and the majority element always exist in the array.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [3,2,3]
<strong>Output:</strong> 3</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>


## Solution
### python
```python
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        majority = nums[0]
        count = 1
        for x in nums[1:]:
            if x == majority:
                count += 1
            else:
                count -= 1
                if count < 0:
                    majority = x
                    count = 0
        return majority



```
### python3
```python3
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        majority = nums[0]
        count = 1
        for x in nums[1:]:
            if x == majority:
                count += 1
            else:
                count -= 1
                if count < 0:
                    majority = x
                    count = 0
        return majority

```

## Author
EINDEX