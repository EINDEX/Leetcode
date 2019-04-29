# Count and Say

## Difficulty
Easy

## Question
<p>The count-and-say sequence is the sequence of integers with the first five terms as following:</p>

<pre>
1.     1
2.     11
3.     21
4.     1211
5.     111221
</pre>

<p><code>1</code> is read off as <code>&quot;one 1&quot;</code> or <code>11</code>.<br />
<code>11</code> is read off as <code>&quot;two 1s&quot;</code> or <code>21</code>.<br />
<code>21</code> is read off as <code>&quot;one 2</code>, then <code>one 1&quot;</code> or <code>1211</code>.</p>

<p>Given an integer <i>n</i>&nbsp;where 1 &le; <em>n</em> &le; 30, generate the <i>n</i><sup>th</sup> term of the count-and-say sequence.</p>

<p>Note: Each term of the sequence of integers will be represented as a string.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 1
<b>Output:</b> &quot;1&quot;
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> 4
<b>Output:</b> &quot;1211&quot;</pre>


## Solution
### python
```python
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        x = '1'
        def inner(x,n):
            if n == 0:
                return '1'
            c = x[0]
            table = []
            tv = 0
            for t in x:
                if t == c:  
                    tv += 1
                elif tv != 0:
                    table.append((tv,c))
                    tv = 1
                    c = t
            if tv:
                table.append((tv, c))
            res = "".join([str(x)+y for x,y in table])
            if n == 1:
                return res
            return inner(res, n-1)
        if n == 0:
            return ''
        else:
            return inner(x, n-1)
        

```
### python3
```python3
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        x = '1'
        def inner(x,n):
            if n == 0:
                return '1'
            c = x[0]
            table = []
            tv = 0
            for t in x:
                if t == c:  
                    tv += 1
                elif tv != 0:
                    table.append((tv,c))
                    tv = 1
                    c = t
            if tv:
                table.append((tv, c))
            res = "".join([str(x)+y for x,y in table])
            if n == 1:
                return res
            return inner(res, n-1)
        if n == 0:
            return ''
        else:
            return inner(x, n-1)
        
```

## Author
EINDEX