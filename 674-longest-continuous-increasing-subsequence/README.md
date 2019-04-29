# Longest Continuous Increasing Subsequence

## Difficulty
Easy

## Question
<p>
Given an unsorted array of integers, find the length of longest <code>continuous</code> increasing subsequence (subarray).
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,3,5,4,7]
<b>Output:</b> 3
<b>Explanation:</b> The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [2,2,2,2,2]
<b>Output:</b> 1
<b>Explanation:</b> The longest continuous increasing subsequence is [2], its length is 1. 
</pre>
</p>

<p><b>Note:</b>
Length of the array will not exceed 10,000.
</p>

## Solution
### python
```python
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        res = 0
        tmp = nums[0] - 1
        count = 0
        for x in range(l):
            if nums[x] > tmp:
                count += 1
                if count > res:
                    res = count
            else:
                count = 1
            tmp = nums[x]
        return res
            



```
### python3
```python3
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        res = 0
        tmp = nums[0] - 1
        count = 0
        for x in range(l):
            if nums[x] > tmp:
                count += 1
                if count > res:
                    res = count
            else:
                count = 1
            tmp = nums[x]
        return res
            

```

## Author
EINDEX