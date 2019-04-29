# Valid Palindrome

## Difficulty
Easy

## Question
<p>Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.</p>

<p><strong>Note:</strong>&nbsp;For the purpose of this problem, we define empty string as valid palindrome.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;A man, a plan, a canal: Panama&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;race a car&quot;
<strong>Output:</strong> false
</pre>


## Solution
### python
```python
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        b = len(s) - 1
        def isV(v):
            if 97 <= ord(v) <= 122:
                return True
            if 65 <= ord(v) <= 90:
                return True
            if 48 <= ord(v) <= 57:
                return True
        while a < b:
            if not isV(s[a]):
                a += 1
                continue
            if not isV(s[b]):
                b -= 1
                continue
            if s[a].lower() == s[b].lower():
                a += 1
                b -= 1
            else:
                return False
        return True

```
### python3
```python3
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [x for x in s.lower() if x in "1234567890asdfghjklqwertyuiopzxcvbnm"]
        return s[::-1] == s
        

```

## Author
EINDEX