# Max Area of Island

## Difficulty
Medium

## Question
<p>Given a non-empty 2D array <code>grid</code> of 0&#39;s and 1&#39;s, an <b>island</b> is a group of <code>1</code>&#39;s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.</p>

<p>Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)</p>

<p><b>Example 1:</b></p>

<pre>
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,<b>1</b>,0,<b>1</b>,0,0],
 [0,1,0,0,1,1,0,0,<b>1</b>,<b>1</b>,<b>1</b>,0,0],
 [0,0,0,0,0,0,0,0,0,0,<b>1</b>,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
</pre>
Given the above grid, return <code>6</code>. Note the answer is not 11, because the island must be connected 4-directionally.

<p><b>Example 2:</b></p>

<pre>
[[0,0,0,0,0,0,0,0]]</pre>
Given the above grid, return <code>0</code>.

<p><b>Note:</b> The length of each dimension in the given <code>grid</code> does not exceed 50.</p>


## Solution
### python
```python
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        res = 0
        h, w = len(grid), len(grid[0])
        def area(x, y):
            if x< 0 or x >= w or y <0 or y>=h:
                return 0
            if grid[y][x]:
                grid[y][x] = 0
                return area(x+1, y) + area(x-1,y) + area(x, y+1) + area(x, y-1) + 1
            return 0
        
        for x in range(w):
            for y in range(h):
                if grid[y][x]:
                    res = max(area(x, y), res)
        return res
                

```
### python3
```python3
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        res = 0
        h, w = len(grid), len(grid[0])
        def area(x, y):
            if x< 0 or x >= w or y <0 or y>=h:
                return 0
            if grid[y][x]:
                grid[y][x] = 0
                return area(x+1, y) + area(x-1,y) + area(x, y+1) + area(x, y-1) + 1
            return 0
        
        for x in range(w):
            for y in range(h):
                if grid[y][x]:
                    res = max(area(x, y), res)
        return res
                
```

## Author
EINDEX