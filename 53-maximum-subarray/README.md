# Maximum Subarray

## Difficulty
Easy

## Question
<p>Given an integer array <code>nums</code>, find the contiguous subarray&nbsp;(containing at least one number) which has the largest sum and return its sum.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [-2,1,-3,4,-1,2,1,-5,4],
<strong>Output:</strong> 6
<strong>Explanation:</strong>&nbsp;[4,-1,2,1] has the largest sum = 6.
</pre>

<p><strong>Follow up:</strong></p>

<p>If you have figured out the O(<em>n</em>) solution, try coding another solution using the divide and conquer approach, which is more subtle.</p>


## Solution
### python3
```python3
#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (41.61%)
# Total Accepted:    33.4K
# Total Submissions: 80.3K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in range(1, len(nums)):
            if nums[x-1] > 0:
                nums[x] += nums[x-1]
        return max(nums)
        


```

## Author
EINDEX