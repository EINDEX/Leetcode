# Longest Common Prefix

## Difficulty
Easy

## Question
<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p><strong>Note:</strong></p>

<p>All given inputs are in lowercase letters <code>a-z</code>.</p>


## Solution
### python
```python
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        length = len(strs)
        
        flag = True
        res = ""
        index = 0
        while flag:
            temp = ""
            for x in range(length):
                if len(strs[x]) > index:
                    if not temp:
                        temp = strs[x][index]
                    else:
                        if temp != strs[x][index]:
                            return res
                else:
                    return res
            else:
                res += temp
            index += 1
                    
                
        


```
### python3
```python3
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        length = len(strs)
        
        flag = True
        res = ""
        index = 0
        while flag:
            temp = ""
            for x in range(length):
                if len(strs[x]) > index:
                    if not temp:
                        temp = strs[x][index]
                    else:
                        if temp != strs[x][index]:
                            return res
                else:
                    return res
            else:
                res += temp
            index += 1
                    
                
        

```

## Author
EINDEX