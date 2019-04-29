# Single Number III

## Difficulty
Medium

## Question
<p>Given an array of numbers <code>nums</code>, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>  <code>[1,2,1,3,2,5]</code>
<strong>Output:</strong> <code>[3,5]</code></pre>

<p><b>Note</b>:</p>

<ol>
	<li>The order of the result is not important. So in the above example, <code>[5, 3]</code> is also correct.</li>
	<li>Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?</li>
</ol>

## Solution
### python
```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set=set()
        for n in nums:
            if n not in num_set:
                num_set.add(n)
            else:
                num_set.remove(n)
        return list(num_set)

```

## Author
EINDEX