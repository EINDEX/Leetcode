# Single Number

## Difficulty
Easy

## Question
<p>Given a <strong>non-empty</strong>&nbsp;array of integers, every element appears <em>twice</em> except for one. Find that single one.</p>

<p><strong>Note:</strong></p>

<p>Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [2,2,1]
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [4,1,2,1,2]
<strong>Output:</strong> 4
</pre>


## Solution
### golang
```golang
func singleNumber(nums []int) int {
	res := 0
	for i, x := range nums {
		print(i)
		res ^= x
	}
	return res
}

```
### python
```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        sum = 0
        for i in nums:
            sum ^=i
        return sum

```
### python3
```python3
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        sum = 0
        for i in nums:
            sum ^=i
        return sum 

```

## Author
EINDEX