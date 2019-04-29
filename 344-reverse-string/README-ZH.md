# Reverse String

## Difficulty
Easy

## Question
<p>Write a function that reverses a string. The input string is given as an array of characters <code>char[]</code>.</p>

<p>Do not allocate extra space for another array, you must do this by <strong>modifying the input array&nbsp;<a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> with O(1) extra memory.</p>

<p>You may assume all the characters consist of <a href="https://en.wikipedia.org/wiki/ASCII#Printable_characters" target="_blank">printable ascii characters</a>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;h&quot;,&quot;e&quot;,&quot;l&quot;,&quot;l&quot;,&quot;o&quot;]</span>
<strong>Output: </strong><span id="example-output-1">[&quot;o&quot;,&quot;l&quot;,&quot;l&quot;,&quot;e&quot;,&quot;h&quot;]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[&quot;H&quot;,&quot;a&quot;,&quot;n&quot;,&quot;n&quot;,&quot;a&quot;,&quot;h&quot;]</span>
<strong>Output: </strong><span id="example-output-2">[&quot;h&quot;,&quot;a&quot;,&quot;n&quot;,&quot;n&quot;,&quot;a&quot;,&quot;H&quot;]</span>
</pre>
</div>
</div>


## Solution
### java
```java
public class Solution {
    public String reverseString(String s) {
        StringBuilder sb=new StringBuilder(s);
        sb.reverse();
        return sb.toString();
    }
}
```
### python
```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        
```
### python3
```python3
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        

```

## Author
EINDEX