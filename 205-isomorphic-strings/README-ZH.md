# Isomorphic Strings

## Difficulty
Easy

## Question
<p>Given two strings <b><i>s</i></b> and <b><i>t</i></b>, determine if they are isomorphic.</p>

<p>Two strings are isomorphic if the characters in <b><i>s</i></b> can be replaced to get <b><i>t</i></b>.</p>

<p>All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <b><i>s</i></b> = <code>&quot;egg&quot;, </code><b><i>t = </i></b><code>&quot;add&quot;</code>
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <b><i>s</i></b> = <code>&quot;foo&quot;, </code><b><i>t = </i></b><code>&quot;bar&quot;</code>
<strong>Output:</strong> false</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> <b><i>s</i></b> = <code>&quot;paper&quot;, </code><b><i>t = </i></b><code>&quot;title&quot;</code>
<strong>Output:</strong> true</pre>

<p><b>Note:</b><br />
You may assume both <b><i>s&nbsp;</i></b>and <b><i>t&nbsp;</i></b>have the same length.</p>


## Solution
### python3
```python3
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        rd = {}
        for a, b in zip(s, t):
            if a not in d:
                d[a] = b
            if b not in rd:
                rd[b] = a
            if d[a] != b or rd[b] != a:
                return False
            
        return True
```

## Author
EINDEX