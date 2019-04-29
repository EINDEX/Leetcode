# Hamming Distance

## Difficulty
Easy

## Question
<p>The <a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.</p>

<p>Given two integers <code>x</code> and <code>y</code>, calculate the Hamming distance.</p>

<p><b>Note:</b><br />
0 &le; <code>x</code>, <code>y</code> &lt; 2<sup>31</sup>.
</p>

<p><b>Example:</b>
<pre>
<b>Input:</b> x = 1, y = 4

<b>Output:</b> 2

<b>Explanation:</b>
1   (0 0 0 1)
4   (0 1 0 0)
       &uarr;   &uarr;

The above arrows point to positions where the corresponding bits are different.
</pre>
</p>

## Solution
### python
```python
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #v2
        return bin(x^y).count('1')
    
        #v1
        a = bin(x)[2:]
        b = bin(y)[2:]
        if len(a) < len(b):
            a='0'*(len(b)-len(a))+a
        else:
            b='0'*(len(a)-len(b))+b
        return sum([a!=b for a,b in zip(a,b)])
        


```

## Author
EINDEX