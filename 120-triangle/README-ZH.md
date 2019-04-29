# Triangle

## Difficulty
Medium

## Question
<p>Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.</p>

<p>For example, given the following triangle</p>

<pre>
[
     [<strong>2</strong>],
    [<strong>3</strong>,4],
   [6,<strong>5</strong>,7],
  [4,<strong>1</strong>,8,3]
]
</pre>

<p>The minimum path sum from top to bottom is <code>11</code> (i.e., <strong>2</strong> + <strong>3</strong> + <strong>5</strong> + <strong>1</strong> = 11).</p>

<p><strong>Note:</strong></p>

<p>Bonus point if you are able to do this using only <em>O</em>(<em>n</em>) extra space, where <em>n</em> is the total number of rows in the triangle.</p>


## Solution
### python
```python
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for l in range(len(triangle)-1-1, -1, -1):
            for x in range(len(triangle[l])):
                triangle[l][x] += min(triangle[l+1][x], triangle[l+1][x+1])
        return triangle[0][0]

```
### python3
```python3
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for l in range(len(triangle)-1-1, -1, -1):
            for x in range(len(triangle[l])):
                triangle[l][x] += min(triangle[l+1][x], triangle[l+1][x+1])
        return triangle[0][0]
```

## Author
EINDEX