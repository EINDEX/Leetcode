# Unique Paths

## Difficulty
Medium

## Question
<p>A robot is located at the top-left corner of a <em>m</em> x <em>n</em> grid (marked &#39;Start&#39; in the diagram below).</p>

<p>The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked &#39;Finish&#39; in the diagram below).</p>

<p>How many possible unique paths are there?</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" style="width: 400px; height: 183px;" /><br />
<small>Above is a 7 x 3 grid. How many possible unique paths are there?</small></p>

<p><strong>Note:</strong> <em>m</em> and <em>n</em> will be at most 100.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> m = 3, n = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong>
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -&gt; Right -&gt; Down
2. Right -&gt; Down -&gt; Right
3. Down -&gt; Right -&gt; Right
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> m = 7, n = 3
<strong>Output:</strong> 28</pre>


## Solution
### python
```python
from functools import reduce
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = lambda z: reduce(lambda x,y :x*y, range(1, z+1)) if z > 0 else 1
        return int(a(m+n-2)/(a(m-1)*a(n-1)))
        
        

```
### python3
```python3
from functools import reduce
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        a = lambda z: reduce(lambda x,y :x*y, range(1, z+1)) if z > 0 else 1
        return int(a(m+n-2)/(a(m-1)*a(n-1)))
        
        
```

## Author
EINDEX