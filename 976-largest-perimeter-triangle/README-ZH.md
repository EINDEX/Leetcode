# Largest Perimeter Triangle

## Difficulty
Easy

## Question
<p>Given an array <code>A</code> of positive lengths, return the largest perimeter of a triangle with <strong>non-zero area</strong>, formed from 3 of these lengths.</p>

<p>If it is impossible to form any&nbsp;triangle of non-zero area, return <code>0</code>.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[2,1,2]</span>
<strong>Output: </strong><span id="example-output-1">5</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,2,1]</span>
<strong>Output: </strong><span id="example-output-2">0</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[3,2,3,4]</span>
<strong>Output: </strong><span id="example-output-3">10</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[3,6,2,3]</span>
<strong>Output: </strong><span id="example-output-4">8</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>3 &lt;= A.length &lt;= 10000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 10^6</code></li>
</ol>
</div>
</div>
</div>
</div>

## Solution
### python3
```python3
#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 最小面积矩形
#
# https://leetcode-cn.com/problems/largest-perimeter-triangle/description/
#
# algorithms
# Easy (57.06%)
# Total Accepted:    1.5K
# Total Submissions: 2.6K
# Testcase Example:  '[2,1,2]'
#
# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
# 
# 如果不能形成任何面积不为零的三角形，返回 0。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：[2,1,2]
# 输出：5
# 
# 
# 示例 2：
# 
# 输入：[1,2,1]
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：[3,2,3,4]
# 输出：10
# 
# 
# 示例 4：
# 
# 输入：[3,6,2,3]
# 输出：8
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= A.length <= 10000
# 1 <= A[i] <= 10^6
# 
# 
#
class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(reverse=True)
        for i in range(len(A) - 3 + 1):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        else:
            return 0        
        


```

## Author
EINDEX