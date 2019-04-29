# Plus One

## Difficulty
Easy

## Question
<p>Given a <strong>non-empty</strong> array of digits&nbsp;representing a non-negative integer, plus one to the integer.</p>

<p>The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.</p>

<p>You may assume the integer does not contain any leading zero, except the number 0 itself.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong> The array represents the integer 123.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [4,3,2,1]
<strong>Output:</strong> [4,3,2,2]
<strong>Explanation:</strong> The array represents the integer 4321.
</pre>

## Solution
### python
```python
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = True
        for x in range(len(digits)-1,0-1,-1):
            # print(x)
            if flag:
                digits[x] += 1
                flag = False
            if digits[x] >= 10:
                flag = True
                digits[x] -= 10
        if flag:
            return [1] + digits
        else:
            return digits


```
### python3
```python3
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = False
        digits[-1] += 1
        for i in range(len(digits)-1, 0-1, -1):
            if flag:
                digits[i] += 1
                flag = False
            if digits[i] >= 10:
                digits[i] -= 10
                flag = True
        else:
            if flag:
                digits = [1] + digits
        return digits
                

```

## Author
EINDEX