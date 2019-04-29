# Two Sum II - Input array is sorted

## Difficulty
Easy

## Question
<p>Given an array of integers that is already <strong><em>sorted in ascending order</em></strong>, find two numbers such that they add up to a specific target number.</p>

<p>The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Your returned answers (both index1 and index2) are not zero-based.</li>
	<li>You may assume that each input would have <em>exactly</em> one solution and you may not use the <em>same</em> element twice.</li>
</ul>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> numbers = [2,7,11,15], target = 9
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.</pre>


## Solution
### python
```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {}
        for i, val in enumerate(numbers):
            if val in cache:
                return sorted([cache[val], i+1])
            else:
                cache[target-val] = i+1
        

```
### python3
```python3
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}
        for i, x in enumerate(numbers):
            if target - x in data:
                return [data[target-x]+1, i+1]
            data[x] = i
```

## Author
EINDEX