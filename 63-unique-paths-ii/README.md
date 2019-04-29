# Unique Paths II

## Difficulty
Medium

## Question
<p>A robot is located at the top-left corner of a <em>m</em> x <em>n</em> grid (marked &#39;Start&#39; in the diagram below).</p>

<p>The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked &#39;Finish&#39; in the diagram below).</p>

<p>Now consider if some obstacles are added to the grids. How many unique paths would there be?</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" style="width: 400px; height: 183px;" /></p>

<p>An obstacle and empty space is marked as <code>1</code> and <code>0</code> respectively in the grid.</p>

<p><strong>Note:</strong> <em>m</em> and <em>n</em> will be at most 100.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
</strong>[
&nbsp; [0,0,0],
&nbsp; [0,1,0],
&nbsp; [0,0,0]
]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -&gt; Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right -&gt; Right
</pre>


## Solution
### python3
```python3
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        w = len(obstacleGrid[0])
        h = len(obstacleGrid)
        
        for x in range(w):
            for y in range(h):
                if x == 0 and y == 0:
                    if obstacleGrid[y][x] != 1:
                        obstacleGrid[y][x] = -1
                    else:
                        obstacleGrid[y][x] = 0
                    continue
                if obstacleGrid[y][x] == 1:
                    obstacleGrid[y][x] = 0
                    continue
                a = obstacleGrid[y-1][x] if y > 0 else 0
                b = obstacleGrid[y][x-1] if x > 0 else 0
                obstacleGrid[y][x] = a + b
        return -obstacleGrid[-1][-1]
```

## Author
EINDEX