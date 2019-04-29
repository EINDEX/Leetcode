# Score After Flipping Matrix

## Difficulty
Medium

## Question
<p>We have a two dimensional matrix&nbsp;<code>A</code> where each value is <code>0</code> or <code>1</code>.</p>

<p>A move consists of choosing any row or column, and toggling each value in that row or column: changing all <code>0</code>s to <code>1</code>s, and all <code>1</code>s to <code>0</code>s.</p>

<p>After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.</p>

<p>Return the highest possible&nbsp;score.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[0,0,1,1],[1,0,1,0],[1,1,0,0]]</span>
<strong>Output: </strong><span id="example-output-1">39</span>
<strong>Explanation:
</strong>Toggled to <span id="example-input-1-1">[[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39</span></pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 20</code></li>
	<li><code>1 &lt;= A[0].length &lt;= 20</code></li>
	<li><code>A[i][j]</code>&nbsp;is <code>0</code> or <code>1</code>.</li>
</ol>
</div>


## Solution
### python
```python
class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # 按行翻转保证第一列的值都为正
        # 第二列往后和小于 1/2 行数是翻转列
        if not A:
            return 0
        
        # 翻转行
        for x in range(len(A)):
            if A[x][0] == 0:  
                for y in range(len(A[x])):
                    if A[x][y] == 0:
                        A[x][y] = 1
                    else:
                        A[x][y] = 0
        s = 0
        # 算和
        for y in range(len(A[0])):
            line_s = sum([A[x][y] for x in range(len(A))])
            s += max(len(A) - line_s, line_s) * (2**(len(A[0])-y-1))
        return s
            

```
### python3
```python3
class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # 按行翻转保证第一列的值都为正
        # 第二列往后和小于 1/2 行数是翻转列
        if not A:
            return 0
        
        # 翻转行
        for x in range(len(A)):
            if A[x][0] == 0:  
                for y in range(len(A[x])):
                    if A[x][y] == 0:
                        A[x][y] = 1
                    else:
                        A[x][y] = 0
        s = 0
        # 算和
        for y in range(len(A[0])):
            line_s = sum([A[x][y] for x in range(len(A))])
            s += max(len(A) - line_s, line_s) * (2**(len(A[0])-y-1))
        return s
            
```

## Author
EINDEX