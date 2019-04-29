# Longest Palindromic Substring

## Difficulty
Medium

## Question
<p>Given a string <strong>s</strong>, find the longest palindromic substring in <strong>s</strong>. You may assume that the maximum length of <strong>s</strong> is 1000.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Note:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>


## Solution
### python
```python
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2 or s == s[::-1]:
            return s
        
        start = 0
        max_len = 0
        # 单字符扩展
        for i in range(l):
            k = max_len // 2
            while i - k >= 0 and i + k < l and s[i-k:i+k+1] == s[i-k:i+k+1][::-1]:
                start = i-k
                max_len = 2*k+1
                k += 1
            k = max_len // 2
            while i - k >= 0 and i + 1 + k < l and s[i-k:i+k+2] == s[i-k:i+k+2][::-1]:
                start = i-k
                max_len = 2*k+2
                k += 1   
        return s[start:start+max_len]

```
### python3
```python3
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        l = len(s)
        # 单字符扩展
        for i in range(l):
            k = 0
            while i - k >= 0 and i + k < l:
                if s[i-k] == s[i+k]:
                    if 2*k+1 > len(res):
                        res = s[i-k:i+k+1]
                else:
                    break
                k += 1
                
        
        # 双字符扩展
        for i in range(l-1):
            k = 0
            while i - k >= 0 and i+1 + k < l:
                if s[i-k] == s[i+1+k]:
                    if 2*k+2 > len(res):
                        res = s[i-k:i+k+2]
                else:
                    break
                k += 1
        return res
```

## Author
EINDEX