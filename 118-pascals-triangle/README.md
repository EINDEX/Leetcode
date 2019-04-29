# Pascal's Triangle

## Difficulty
Easy

## Question
<p>Given a non-negative integer&nbsp;<em>numRows</em>, generate the first <em>numRows</em> of Pascal&#39;s triangle.</p>

<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px" /><br />
<small>In Pascal&#39;s triangle, each number is the sum of the two numbers directly above it.</small></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 5
<strong>Output:</strong>
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
</pre>


## Solution
### golang
```golang
func generate(numRows int) [][]int {
	res := make([][]int, numRows)
	for r := 0; r < numRows; r++ {
		res[r] = make([]int, r+1)
		if r == 0 {
			res[0][0] = 1
		} else {
			for i := 0; i < r+1; i++ {
				if (i == 0) || (i == r) {
					res[r][i] = 1
				} else {
					res[r][i] = res[r-1][i] + res[r-1][i-1]
				}
			}
		}
	}
	return res
}

```
### python3
```python3
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for x in range(1, numRows+1):
            if x == 1:
                res.append([1])
            else:
                line = []
                for i in range(x):
                    if i == 0:
                        line.append(1)
                    elif i == x - 1:
                        line.append(1)
                    else:
                        line.append(res[-1][i-1]+res[-1][i])
                res.append(line)
        return res
    

```

## Author
EINDEX