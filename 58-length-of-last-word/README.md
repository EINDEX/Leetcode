# Length of Last Word

## Difficulty
Easy

## Question
<p>Given a string <i>s</i> consists of upper/lower-case alphabets and empty space characters <code>' '</code>, return the length of last word in the string.</p>

<p>If the last word does not exist, return 0.</p>

<p><b>Note:</b> A word is defined as a character sequence consists of non-space characters only.</p>

<p><b>Example:</b>
<pre>
<b>Input:</b> "Hello World"
<b>Output:</b> 5
</pre>
</p>

## Solution
### python3
```python3
#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (28.32%)
# Total Accepted:    15.7K
# Total Submissions: 55.4K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 
# 如果不存在最后一个单词，请返回 0 。
# 
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 
# 示例:
# 
# 输入: "Hello World"
# 输出: 5
# 
# 
#
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = s.split()
        if not r:
            return 0
        return len(r[-1])
        


```

## Author
EINDEX