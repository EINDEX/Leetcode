# Move Zeroes

## Difficulty
Easy

## Question
<p>Given an array <code>nums</code>, write a function to move all <code>0</code>&#39;s to the end of it while maintaining the relative order of the non-zero elements.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> <code>[0,1,0,3,12]</code>
<b>Output:</b> <code>[1,3,12,0,0]</code></pre>

<p><b>Note</b>:</p>

<ol>
	<li>You must do this <b>in-place</b> without making a copy of the array.</li>
	<li>Minimize the total number of operations.</li>
</ol>

## Solution
### python
```python
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        zi = len(nums)
        flag = False
        for i in range(len(nums)):
            if nums[i] == 0 and not flag:
                zi = i
                flag = True
            elif zi < len(nums):
                nums[i], nums[zi] = nums[zi], nums[i]
                while zi<len(nums) and  nums[zi]:
                    zi += 1

```
### python3
```python3
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        zi = len(nums)
        flag = False
        for i in range(len(nums)):
            if nums[i] == 0 and not flag:
                zi = i
                flag = True
            elif zi < len(nums):
                nums[i], nums[zi] = nums[zi], nums[i]
                while zi<len(nums) and  nums[zi]:
                    zi += 1
```

## Author
EINDEX