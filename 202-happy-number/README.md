# Happy Number

## Difficulty
Easy

## Question
<p>Write an algorithm to determine if a number is &quot;happy&quot;.</p>

<p>A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.</p>

<p><strong>Example:&nbsp;</strong></p>

<pre>
<strong>Input:</strong> 19
<strong>Output:</strong> true
<strong>Explanation: 
</strong>1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</pre>

## Solution
### python3
```python3
#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# https://leetcode-cn.com/problems/happy-number/description/
#
# algorithms
# Easy (51.19%)
# Total Accepted:    10.7K
# Total Submissions: 20.8K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数是不是“快乐数”。
#
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到
# 1。如果可以变为 1，那么这个数就是快乐数。
#
# 示例: 
#
# 输入: 19
# 输出: true
# 解释:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#
#
#


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1:
            s.add(n)
            r = 0
            while n:
                r += (n % 10)**2
                n = n // 10
            n = r
            if n in s:
                return False
        return True

```

## Author
EINDEX