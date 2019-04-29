# Partition Labels

## Difficulty
Medium

## Question
<p>
A string <code>S</code> of lowercase letters is given.  We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
</p><p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> S = "ababcbacadefegdehijhklij"
<b>Output:</b> [9,7,8]
<b>Explanation:</b>
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
</pre>
</p>

<p><b>Note:</b><br><ol>
<li><code>S</code> will have length in range <code>[1, 500]</code>.</li>
<li><code>S</code> will consist of lowercase letters (<code>'a'</code> to <code>'z'</code>) only.</li>
</ol></p>

## Solution
### python
```python
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        d = {k:i for i,k in enumerate(list(S))}
        res = []
        lattes = set()
        index = 0
        for i, x in enumerate(list(S)):
            if x not in lattes:
                if all(i > d[k] for k in list(lattes)) and i != 0:
                    lattes = set()
                    res.append(i - sum(res))
                    
                lattes.add(x)
        if res:
            res.append(len(S)-sum(res))
        else:
            res.append(len(S))
        return res

```
### python3
```python3
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        d = {k:i for i,k in enumerate(list(S))}
        res = []
        lattes = set()
        index = 0
        for i, x in enumerate(list(S)):
            if x not in lattes:
                if all(i > d[k] for k in list(lattes)) and i != 0:
                    print(lattes)
                    lattes = set()
                    res.append(i - sum(res))
                    
                lattes.add(x)
        if res:
            res.append(len(S)-sum(res))
        else:
            res.append(len(S))
        print(res)
        return res
```

## Author
EINDEX