# First Unique Character in a String

## Difficulty
Easy

## Question
<p>
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
</p>
<p><b>Examples:</b>
<pre>
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
</pre>
</p>

<p>
<b>Note:</b> You may assume the string contain only lowercase letters.
</p>

## Solution
### python
```python
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        bucket = {chr(k):0 for k in range(97,123)}
        for i, k in enumerate(s):
            if bucket[k] == 0:
                bucket[k] = i+1
            elif bucket[k] > 0:
                bucket[k] = -1
       
        for i, k in enumerate(s):
            if bucket[k] > 0:
                return i
        else:
            return -1


```
### python3
```python3
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        bucket = {chr(k):0 for k in range(97,123)}
        for i, k in enumerate(s):
            if bucket[k] == 0:
                bucket[k] = i+1
            elif bucket[k] > 0:
                bucket[k] = -1
       
        for i, k in enumerate(s):
            if bucket[k] > 0:
                return i
        else:
            return -1
```

## Author
EINDEX