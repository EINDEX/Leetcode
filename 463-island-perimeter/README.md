# Island Perimeter

## Difficulty
Easy

## Question
<p>You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.</p>

<p>Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).</p>

<p>The island doesn&#39;t have &quot;lakes&quot; (water inside that isn&#39;t connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don&#39;t exceed 100. Determine the perimeter of the island.</p>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
<strong>Input:</strong>
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

<strong>Output:</strong> 16

<strong>Explanation:</strong> The perimeter is the 16 yellow stripes in the image below:

<img src="https://assets.leetcode.com/uploads/2018/10/12/island.png" style="width: 221px; height: 213px;" />
</pre>


## Solution
### python
```python
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid[0])
        cos = len(grid)
        s = 0
        for r in range(row):
            for c in range(cos):
                if grid[c][r]:
                    count = 0
                    if r > 0:
                        if grid[c][r-1]:
                            count += 1
                    if r < row - 1:
                        if grid[c][r+1]:
                            count += 1
                    if c > 0:
                        if grid[c-1][r]:
                            count += 1
                    if c < cos - 1:
                        if grid[c+1][r]:
                            count += 1
                    s += 4 - count
        return s
        


```

## Author
EINDEX