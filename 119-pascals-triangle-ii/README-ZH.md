# Pascal's Triangle II

## Difficulty
Easy

## Question
<p>Given a non-negative&nbsp;index <em>k</em>&nbsp;where <em>k</em> &le;&nbsp;33, return the <em>k</em><sup>th</sup>&nbsp;index row of the Pascal&#39;s triangle.</p>

<p>Note that the row index starts from&nbsp;0.</p>

<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" /><br />
<small>In Pascal&#39;s triangle, each number is the sum of the two numbers directly above it.</small></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 3
<strong>Output:</strong> [1,3,3,1]
</pre>

<p><strong>Follow up:</strong></p>

<p>Could you optimize your algorithm to use only <em>O</em>(<em>k</em>) extra space?</p>


## Solution
### python
```python
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        res = [0 for x in range(rowIndex+1)]
        res[0],res[1] = 1, 1
        for x in range(1, rowIndex):
            for k in range(x,0-1,-1):
                res[k+1] = res[k] + res[k+1]
            res[x+1] = 1
        return res
            
            
        

```
### python3
```python3
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        res = [0 for x in range(rowIndex+1)]
        res[0],res[1] = 1, 1
        for x in range(1, rowIndex):
            for k in range(x,0-1,-1):
                res[k+1] = res[k] + res[k+1]
            res[x+1] = 1
        return res
            
            
        
```

## Author
EINDEX