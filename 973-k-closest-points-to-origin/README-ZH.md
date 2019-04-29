# K Closest Points to Origin

## Difficulty
Medium

## Question
<p>We have a list of <code>points</code>&nbsp;on the plane.&nbsp; Find the <code>K</code> closest points to the origin <code>(0, 0)</code>.</p>

<p>(Here, the distance between two points on a plane is the Euclidean distance.)</p>

<p>You may return the answer in any order.&nbsp; The&nbsp;answer is guaranteed to be unique (except for the order that it is in.)</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>points = <span id="example-input-1-1">[[1,3],[-2,2]]</span>, K = <span id="example-input-1-2">1</span>
<strong>Output: </strong><span id="example-output-1">[[-2,2]]</span>
<strong>Explanation: </strong>
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) &lt; sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>points = <span id="example-input-2-1">[[3,3],[5,-1],[-2,4]]</span>, K = <span id="example-input-2-2">2</span>
<strong>Output: </strong><span id="example-output-2">[[3,3],[-2,4]]</span>
(The answer [[-2,4],[3,3]] would also be accepted.)
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= K &lt;= points.length &lt;= 10000</code></li>
	<li><code>-10000 &lt; points[i][0] &lt; 10000</code></li>
	<li><code>-10000 &lt; points[i][1] &lt; 10000</code></li>
</ol>
</div>
</div>

## Solution
### python3
```python3
#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 戳印序列
#
# https://leetcode-cn.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Easy (65.68%)
# Total Accepted:    1.5K
# Total Submissions: 2.3K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# 我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。
# 
# （这里，平面上两点之间的距离是欧几里德距离。）
# 
# 你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。
# 
# 
# 
# 示例 1：
# 
# 输入：points = [[1,3],[-2,2]], K = 1
# 输出：[[-2,2]]
# 解释： 
# (1, 3) 和原点之间的距离为 sqrt(10)，
# (-2, 2) 和原点之间的距离为 sqrt(8)，
# 由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
# 我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
# 
# 
# 示例 2：
# 
# 输入：points = [[3,3],[5,-1],[-2,4]], K = 2
# 输出：[[3,3],[-2,4]]
# （答案 [[-2,4],[3,3]] 也会被接受。）
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
# 
# 
#

from heapq import *

class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        h = []
        for p in points:
            heappush(h, (p[0]*p[0]+p[1]*p[1], p))
        return [heappop(h)[1] for _ in range(K)]
        


```

## Author
EINDEX