# Transpose Matrix

## Difficulty
Easy

## Question
<p>Given a&nbsp;matrix <code>A</code>, return the transpose of <code>A</code>.</p>

<p>The transpose of a matrix is the matrix flipped over it&#39;s main diagonal, switching the row and column indices of the matrix.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,2,3],[4,5,6],[7,8,9]]</span>
<strong>Output: </strong><span id="example-output-1">[[1,4,7],[2,5,8],[3,6,9]]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[1,2,3],[4,5,6]]</span>
<strong>Output: </strong><span id="example-output-2">[[1,4],[2,5],[3,6]]</span>
</pre>

<p>&nbsp;</p>

<p><span><strong>Note:</strong></span></p>

<ol>
	<li><code><span>1 &lt;= A.length&nbsp;&lt;= 1000</span></code></li>
	<li><code><span>1 &lt;= A[0].length&nbsp;&lt;= 1000</span></code></li>
</ol>
</div>
</div>


## Solution
### python
```python
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[x][y] for x in range(len(A))] for y in range(len(A[0]))]
        
        

```
### python3
```python3
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[A[x][y] for x in range(len(A))] for y in range(len(A[0]))]
        return res
        
        
```

## Author
EINDEX