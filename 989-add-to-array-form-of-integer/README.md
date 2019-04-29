# Add to Array-Form of Integer

## Difficulty
Easy

## Question
<p>For a non-negative integer <code>X</code>, the&nbsp;<em>array-form of <code>X</code></em>&nbsp;is an array of its digits in left to right order.&nbsp; For example, if <code>X = 1231</code>, then the array form is&nbsp;<code>[1,2,3,1]</code>.</p>

<p>Given the array-form <code>A</code> of a non-negative&nbsp;integer <code>X</code>, return the array-form of the integer <code>X+K</code>.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,2,0,0]</span>, K = 34
<strong>Output: </strong><span id="example-output-1">[1,2,3,4]</span>
<strong>Explanation: </strong>1200 + 34 = 1234
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[2,7,4]</span>, K = <span id="example-input-2-2">181</span>
<strong>Output: </strong><span id="example-output-2">[4,5,5]</span>
<strong>Explanation: </strong>274 + 181 = 455
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[2,1,5]</span>, K = <span id="example-input-3-2">806</span>
<strong>Output: </strong><span id="example-output-3">[1,0,2,1]</span>
<strong>Explanation: </strong>215 + 806 = 1021
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-4-1">[9,9,9,9,9,9,9,9,9,9]</span>, K = <span id="example-input-4-2">1</span>
<strong>Output: </strong><span id="example-output-4">[1,0,0,0,0,0,0,0,0,0,0]</span>
<strong>Explanation: </strong>9999999999 + 1 = 10000000000
</pre>

<p>&nbsp;</p>

<p><strong>Note：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 9</code></li>
	<li><code>0 &lt;= K &lt;= 10000</code></li>
	<li>If <code>A.length &gt; 1</code>, then <code>A[0] != 0</code></li>
</ol>
</div>
</div>
</div>
</div>

## Solution
### python3
```python3
#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 按公因数计算最大组件大小
#
# https://leetcode-cn.com/problems/add-to-array-form-of-integer/description/
#
# algorithms
# Easy (33.46%)
# Total Accepted:    270
# Total Submissions: 807
# Testcase Example:  '[1,2,0,0]\n34'
#
# 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
# 
# 给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：A = [1,2,0,0], K = 34
# 输出：[1,2,3,4]
# 解释：1200 + 34 = 1234
# 
# 
# 解释 2：
# 
# 输入：A = [2,7,4], K = 181
# 输出：[4,5,5]
# 解释：274 + 181 = 455
# 
# 
# 示例 3：
# 
# 输入：A = [2,1,5], K = 806
# 输出：[1,0,2,1]
# 解释：215 + 806 = 1021
# 
# 
# 示例 4：
# 
# 输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
# 输出：[1,0,0,0,0,0,0,0,0,0,0]
# 解释：9999999999 + 1 = 10000000000
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 10000
# 0 <= A[i] <= 9
# 0 <= K <= 10000
# 如果 A.length > 1，那么 A[0] != 0
# 
# 
#
class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        a = 0
        B = A[::-1]
        for x in range(len(A)):
            a += B[x] * (10 ** x)
        r = a + K
        return [ int(i) for i in list(str(r))]


```

## Author
EINDEX