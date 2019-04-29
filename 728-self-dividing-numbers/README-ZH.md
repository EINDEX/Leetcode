# Self Dividing Numbers

## Difficulty
Easy

## Question
<p>
A <i>self-dividing number</i> is a number that is divisible by every digit it contains.
</p><p>
For example, 128 is a self-dividing number because <code>128 % 1 == 0</code>, <code>128 % 2 == 0</code>, and <code>128 % 8 == 0</code>.
</p><p>
Also, a self-dividing number is not allowed to contain the digit zero.
</p><p>
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
</p>
<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
left = 1, right = 22
<b>Output:</b> [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
</pre>
</p>

<p><b>Note:</b>
<li>The boundaries of each input argument are <code>1 <= left <= right <= 10000</code>.</li>
</p>

## Solution
### python
```python
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for x in range(left, right+1):
            if all([i!='0' and x%int(i)==0 for i in list(str(x))]):
                res.append(x)
        return res

```
### python3
```python3
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for x in range(left, right+1):
            if all([i!='0' and x%int(i)==0 for i in list(str(x))]):
                res.append(x)
        return res
```

## Author
EINDEX