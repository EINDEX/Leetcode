# Excel Sheet Column Number

## Difficulty
Easy

## Question
<p>Given a column title as appear in an Excel sheet, return its corresponding column number.</p>

<p>For example:</p>

<pre>
    A -&gt; 1
    B -&gt; 2
    C -&gt; 3
    ...
    Z -&gt; 26
    AA -&gt; 27
    AB -&gt; 28 
    ...
</pre>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;A&quot;
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>&quot;AB&quot;
<strong>Output:</strong> 28
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>&quot;ZY&quot;
<strong>Output:</strong> 701
</pre>

## Solution
### python
```python
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum([(ord(x)-(ord('A')-1))*(26**(len(s)-i-1))  for i, x in enumerate(list(s))])
        

```
### python3
```python3
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum([(ord(x)-(ord('A')-1))*(26**(len(s)-i-1))  for i, x in enumerate(list(s))])
        
```

## Author
EINDEX