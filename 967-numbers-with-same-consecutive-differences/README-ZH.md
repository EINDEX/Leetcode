# Numbers With Same Consecutive Differences

## Difficulty
Medium

## Question
<p>Return all <strong>non-negative</strong> integers of length <code>N</code> such that the absolute difference between every two consecutive digits is <code>K</code>.</p>

<p>Note that <strong>every</strong> number in the answer <strong>must not</strong> have leading zeros <strong>except</strong> for the number <code>0</code> itself. For example, <code>01</code> has one leading zero and is invalid, but <code>0</code> is valid.</p>

<p>You may return the answer in any order.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-1-1">3</span>, K = <span id="example-input-1-2">7</span>
<strong>Output: </strong><span id="example-output-1">[181,292,707,818,929]</span>
<strong>Explanation: </strong>Note that 070 is not a valid number, because it has leading zeroes.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-2-1">2</span>, K = <span id="example-input-2-2">1</span>
<strong>Output: </strong><span id="example-output-2">[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]</span></pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 9</code></li>
	<li><code>0 &lt;= K &lt;= 9</code></li>
</ol>


## Solution
### python
```python
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [0,1,2,3,4,5,6,7,8,9]
        if N == 0:
            return []
       
        res = []
        def inner(num, N, K):
            if N == 0:
                res.append(num)
                return
            yushu = num % 10
            if K != 0:
                if yushu - K >= 0:
                    inner(num*10+yushu-K, N-1, K)
                if yushu + K < 10:
                    inner(num*10+yushu+K, N-1, K)
            else:
                inner(num*10+yushu, N-1, K)
        for n in range(1, 10):
            inner(n, N-1, K)
        return res     
        

```
### python3
```python3
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [0,1,2,3,4,5,6,7,8,9]
        if N == 0:
            return []
       
        res = []
        def inner(num, N, K):
            if N == 0:
                res.append(num)
                return
            yushu = num % 10
            if K != 0:
                if yushu - K >= 0:
                    inner(num*10+yushu-K, N-1, K)
                if yushu + K < 10:
                    inner(num*10+yushu+K, N-1, K)
            else:
                inner(num*10+yushu, N-1, K)
        for n in range(1, 10):
            inner(n, N-1, K)
        return res     
        
```

## Author
EINDEX