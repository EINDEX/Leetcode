# Largest Time for Given Digits

## Difficulty
Easy

## Question
<p>Given an array of 4 digits, return the largest 24 hour time that can be made.</p>

<p>The smallest 24 hour time is 00:00, and the largest is 23:59.&nbsp; Starting from 00:00, a time is larger if more time has elapsed since midnight.</p>

<p>Return the answer as a string of length 5.&nbsp; If no valid time can be made, return an empty string.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3,4]</span>
<strong>Output: </strong><span id="example-output-1">&quot;23:41&quot;</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[5,5,5,5]</span>
<strong>Output: </strong><span id="example-output-2">&quot;&quot;</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>A.length == 4</code></li>
	<li><code>0 &lt;= A[i] &lt;= 9</code></li>
</ol>
</div>
</div>

## Solution
### python3
```python3
#
# @lc app=leetcode.cn id=949 lang=python3
#
# [949] 猫和老鼠
#
# https://leetcode-cn.com/problems/largest-time-for-given-digits/description/
#
# algorithms
# Easy (27.98%)
# Total Accepted:    780
# Total Submissions: 2.8K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
# 
# 最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。
# 
# 以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,4]
# 输出："23:41"
# 
# 
# 示例 2：
# 
# 输入：[5,5,5,5]
# 输出：""
# 
# 
# 
# 
# 提示：
# 
# 
# A.length == 4
# 0 <= A[i] <= 9
# 
# 
#
class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A.sort()
        for x in range(23, -1, -1):
            x = str(x)
            if len(x) == 1:
                x = '0' + x
            print(x)
            if int(x[0]) != int(x[1]):
                if int(x[0]) not in A or int(x[1]) not in A:
                    continue
            else:
                if A.count(int(x[0])) < 2:
                    continue
            for y in range(59, -1, -1):
                y = str(y)
                if len(y) == 1:
                    y = '0' + y
                r = [int(c) for c in x + y]
                r.sort()
                if all([r[x] == A[x] for x in range(4)]):
                    return x + ':' + y 
        return ''


```

## Author
EINDEX