# Shortest Distance to a Character

## Difficulty
Easy

## Question
<p>Given a string <code>S</code>&nbsp;and a character <code>C</code>, return an array of integers representing the shortest distance from the character <code>C</code> in the string.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;loveleetcode&quot;, C = &#39;e&#39;
<strong>Output:</strong> [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>S</code> string length is&nbsp;in&nbsp;<code>[1, 10000].</code></li>
	<li><code>C</code>&nbsp;is a single character, and guaranteed to be in string <code>S</code>.</li>
	<li>All letters in <code>S</code> and <code>C</code> are lowercase.</li>
</ol>


## Solution
### python
```python
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = [10000 for _ in range(len(S))]
        has_C = False
        last_C = 0
        for x in range(len(S)):
            if S[x] == C:
                has_C = True
                last_C = x
            if has_C:
                res[x] = x - last_C
        has_C = False
        last_C = 0
        for x in range(len(S)-1,0-1,-1):
            if S[x] == C:
                has_C = True
                last_C = x
            if has_C and last_C - x < res[x]:
                res[x] = last_C - x
        
        return res

```
### python3
```python3
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = [10000 for _ in range(len(S))]
        has_C = False
        last_C = 0
        for x in range(len(S)):
            if S[x] == C:
                has_C = True
                last_C = x
            if has_C:
                res[x] = x - last_C
        has_C = False
        last_C = 0
        for x in range(len(S)-1,0-1,-1):
            if S[x] == C:
                has_C = True
                last_C = x
            if has_C and last_C - x < res[x]:
                res[x] = last_C - x
        
        return res
```

## Author
EINDEX