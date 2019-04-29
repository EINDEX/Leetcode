# Palindrome Partitioning

## Difficulty
Medium

## Question
<p>Given a string <em>s</em>, partition <em>s</em> such that every substring of the partition is a palindrome.</p>

<p>Return all possible palindrome partitioning of <em>s</em>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;&quot;aab&quot;
<strong>Output:</strong>
[
  [&quot;aa&quot;,&quot;b&quot;],
  [&quot;a&quot;,&quot;a&quot;,&quot;b&quot;]
]
</pre>


## Solution
### python
```python
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def inner(l, s): 
            if s and len(s) > 1:
                for x in range(1, len(s)+1):
                    if s[:x] == s[:x][::-1]:
                        c = l[:]
                        c.append(s[:x])
                        inner(c, s[x:])
            else:
                c = l[:]
                if s:   
                    c.append(s)
                if all([x==x[::-1] for x in c]):
                    res.append(c)             
        inner([], s)
        return res
        

```
### python3
```python3
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def inner(l, s): 
            if s and len(s) > 1:
                for x in range(1, len(s)+1):
                    if s[:x] == s[:x][::-1]:
                        c = l[:]
                        c.append(s[:x])
                        inner(c, s[x:])
            else:
                c = l[:]
                if s:   
                    c.append(s)
                if all([x==x[::-1] for x in c]):
                    res.append(c)             
        inner([], s)
        return res
        
```

## Author
EINDEX