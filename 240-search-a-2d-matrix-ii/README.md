# Search a 2D Matrix II

## Difficulty
Medium

## Question
<p>Write an efficient algorithm that searches for a value in an <i>m</i> x <i>n</i> matrix. This matrix has the following properties:</p>

<ul>
	<li>Integers in each row are sorted in ascending from left to right.</li>
	<li>Integers in each column are sorted in ascending from top to bottom.</li>
</ul>

<p><strong>Example:</strong></p>

<p>Consider the following matrix:</p>

<pre>
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
</pre>

<p>Given&nbsp;target&nbsp;=&nbsp;<code>5</code>, return&nbsp;<code>true</code>.</p>

<p>Given&nbsp;target&nbsp;=&nbsp;<code>20</code>, return&nbsp;<code>false</code>.</p>


## Solution
### python3
```python3
class Solution:
    def searchMatrix(self, m, target):
        """
        :type m: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not m:
            return False
        w = len(m[0])
        h = len(m)
        x = w - 1
        while x >= 0:
            if m[0][x] < target:
                for y in range(1, h):
                    if m[y][x] == target:
                        return True
            elif m[0][x] == target:
                return True
            x -= 1
        return False
            
```

## Author
EINDEX