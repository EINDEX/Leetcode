# Reverse Vowels of a String

## Difficulty
Easy

## Question
<p>Write a function that takes a string as input and reverse only the vowels of a string.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;hello&quot;</span>
<strong>Output: </strong><span id="example-output-1">&quot;holle&quot;</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;leetcode&quot;</span>
<strong>Output: </strong><span id="example-output-2">&quot;leotcede&quot;</span></pre>
</div>

<p><b>Note:</b><br />
The vowels does not include the letter &quot;y&quot;.</p>

<p>&nbsp;</p>


## Solution
### python
```python
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuan = set('aeiouAEIOU')
        s = list(s)
        a, b = 0, len(s) - 1
        while a < b:
            if s[a] not in yuan:
                a += 1
                continue
            if s[b] not in yuan:
                b -= 1
                continue
            s[a], s[b] = s[b],  s[a]
            a += 1
            b -= 1
        return ''.join(s)
        
        

```
### python3
```python3
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuan = ('a', 'e', 'i', 'o', 'u', 'A','E','I','O', 'U')
        r = []
        for x in range(len(s)):
            if s[x] in yuan:
                r.append(s[x])
        k = 1
        s = list(s)
        for x in range(len(s)):
            if s[x] in yuan:
                s[x] = r[-k]
                k += 1
        return ''.join(s)
        
        
```

## Author
EINDEX