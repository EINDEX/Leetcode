# Word Pattern

## Difficulty
Easy

## Question
<p>Given a <code>pattern</code> and a string <code>str</code>, find if <code>str</code> follows the same pattern.</p>

<p>Here <b>follow</b> means a full match, such that there is a bijection between a letter in <code>pattern</code> and a <b>non-empty</b> word in <code>str</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> pattern = <code>&quot;abba&quot;</code>, str = <code>&quot;dog cat cat dog&quot;</code>
<strong>Output:</strong> true</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>pattern = <code>&quot;abba&quot;</code>, str = <code>&quot;dog cat cat fish&quot;</code>
<strong>Output:</strong> false</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> pattern = <code>&quot;aaaa&quot;</code>, str = <code>&quot;dog cat cat dog&quot;</code>
<strong>Output:</strong> false</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> pattern = <code>&quot;abba&quot;</code>, str = <code>&quot;dog dog dog dog&quot;</code>
<strong>Output:</strong> false</pre>

<p><b>Notes:</b><br />
You may assume <code>pattern</code> contains only lowercase letters, and <code>str</code> contains lowercase letters that may be separated by a single space.</p>


## Solution
### python3
```python3
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        d = {}
        rd = {}
        
        for a, b in zip(pattern, words):
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