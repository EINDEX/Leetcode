# Valid Parentheses

## Difficulty
Easy

## Question
<p>Given a string containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
</ol>

<p>Note that an empty string is&nbsp;also considered valid.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;()&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;()[]{}&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> &quot;(]&quot;
<strong>Output:</strong> false
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> &quot;([)]&quot;
<strong>Output:</strong> false
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> &quot;{[]}&quot;
<strong>Output:</strong> true
</pre>


## Solution
### python
```python
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        flag = True
        for x in range(len(s)):
            if s[x] in t:
                if stack:
                    if stack[-1] == t[s[x]]:
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(s[x])
        if stack:
            return False
        return True

```
### python3
```python3
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for x in s:
            if x == ']':
                if not stack:
                    return False
                if stack[-1] == '[':
                        stack.pop(-1)
                else:
                        return False
            elif x == '}':
                    if not stack:
                        return False
                    if stack[-1] == '{':
                        stack.pop(-1)
                    else:
                        return False
            elif x == ')':
                    if not stack:
                        return False
                    if stack[-1] == '(':
                        stack.pop(-1)
                    else:
                        return False
            
            else:
                stack.append(x)
        if stack:
            return False
        return True
        
```

## Author
EINDEX