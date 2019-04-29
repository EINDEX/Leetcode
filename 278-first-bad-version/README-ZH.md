# First Bad Version

## Difficulty
Easy

## Question
<p>You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.</p>

<p>Suppose you have <code>n</code> versions <code>[1, 2, ..., n]</code> and you want to find out the first bad one, which causes all the following ones to be bad.</p>

<p>You are given an API <code>bool isBadVersion(version)</code> which will return whether <code>version</code> is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.</p>

<p><b>Example:</b></p>

<pre>
Given n = 5, and version = 4 is the first bad version.

<code>call isBadVersion(3) -&gt; false
call isBadVersion(5)&nbsp;-&gt; true
call isBadVersion(4)&nbsp;-&gt; true

Then 4 is the first bad version.&nbsp;</code>
</pre>

## Solution
### python
```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l < h:
            m = l + (h - l) // 2
            if not isBadVersion(m):
                l = m + 1
            else:
                h = m
        
        return l
        

```
### python3
```python3
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l < h:
            m = l + (h - l) // 2
            if not isBadVersion(m):
                l = m + 1
            else:
                h = m
        
        return l
        
```

## Author
EINDEX