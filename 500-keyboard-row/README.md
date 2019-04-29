# Keyboard Row

## Difficulty
Easy

## Question
<p>Given a List of words, return the words that can be typed using letters of <b>alphabet</b> on only one row&#39;s of American keyboard like the image below.</p>

<p>&nbsp;</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2018/10/12/keyboard.png" style="width: 100%; max-width: 600px" /></p>
&nbsp;

<p><b>Example:</b></p>

<pre>
<b>Input:</b> [&quot;Hello&quot;, &quot;Alaska&quot;, &quot;Dad&quot;, &quot;Peace&quot;]
<b>Output:</b> [&quot;Alaska&quot;, &quot;Dad&quot;]
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>You may use one character in the keyboard more than once.</li>
	<li>You may assume the input string will only contain letters of alphabet.</li>
</ol>


## Solution
### python
```python
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r = []
        row = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        for word in words:
            for i in range(3):
                flag = True
                for a in word.lower():
                    if a not in row[i]:
                        flag = False
                if flag:
                    r.append(word)
        return r
                        
                
            
```

## Author
EINDEX