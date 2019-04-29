# Complex Number Multiplication

## Difficulty
Medium

## Question
<p>
Given two strings representing two <a href = "https://en.wikipedia.org/wiki/Complex_number">complex numbers</a>.</p>

<p>
You need to return a string representing their multiplication. Note i<sup>2</sup> = -1 according to the definition.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "1+1i", "1+1i"
<b>Output:</b> "0+2i"
<b>Explanation:</b> (1 + i) * (1 + i) = 1 + i<sup>2</sup> + 2 * i = 2i, and you need convert it to the form of 0+2i.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "1+-1i", "1+-1i"
<b>Output:</b> "0+-2i"
<b>Explanation:</b> (1 - i) * (1 - i) = 1 + i<sup>2</sup> - 2 * i = -2i, and you need convert it to the form of 0+-2i.
</pre>
</p>

<p><b>Note:</b>
<ol>
<li>The input strings will not have extra blank.</li>
<li>The input strings will be given in the form of <b>a+bi</b>, where the integer <b>a</b> and <b>b</b> will both belong to the range of [-100, 100]. And <b>the output should be also in this form</b>.</li>
</ol>
</p>

## Solution
### python
```python
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x0,x1 = self.u(a)
        y0,y1 = self.u(b)
        return "%s+%si" % (x0*y0-x1*y1,x0*y1+x1*y0)
        
    def u(self,str):
        a = ''
        b = ''
        flag = True
        for n in str[:-1]:
            if flag:
                a+=n
                if n==u'+':
                    flag = False
            else:
                b+=n
        return int(a[:-1]),int(b)

```

## Author
EINDEX