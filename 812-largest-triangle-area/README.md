# Largest Triangle Area

## Difficulty
Easy

## Question
<p>You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The five points are show in the figure below. The red triangle is the largest.
</pre>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png" style="height:328px; width:400px" /></p>

<p><strong>Notes: </strong></p>

<ul>
	<li><code>3 &lt;= points.length &lt;= 50</code>.</li>
	<li>No points will be duplicated.</li>
	<li>&nbsp;<code>-50 &lt;= points[i][j] &lt;= 50</code>.</li>
	<li>Answers within&nbsp;<code>10^-6</code>&nbsp;of the true value will be accepted as correct.</li>
</ul>

<p>&nbsp;</p>


## Solution
### python
```python
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                           -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        return max(area(*triangle)
            for triangle in itertools.combinations(points, 3))
        

```
### python3
```python3
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                           -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        return max(area(*triangle)
            for triangle in itertools.combinations(points, 3))
        
```

## Author
EINDEX