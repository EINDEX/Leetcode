# Find All Numbers Disappeared in an Array

## Difficulty
Easy

## Question
<p>Given an array of integers where 1 &le; a[i] &le; <i>n</i> (<i>n</i> = size of array), some elements appear twice and others appear once.</p>

<p>Find all the elements of [1, <i>n</i>] inclusive that do not appear in this array.</p>

<p>Could you do it without extra space and in O(<i>n</i>) runtime? You may assume the returned list does not count as extra space.</p>

<p><b>Example:</b>
<pre>
<b>Input:</b>
[4,3,2,7,8,2,3,1]

<b>Output:</b>
[5,6]
</pre>
</p>

## Solution
### python
```python
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        return list({x for x in range(1,len(nums)+1)} - set(nums)) if nums else []


```
### python3
```python3
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        return list({x for x in range(1,len(nums)+1)} - set(nums)) if nums else []

```

## Author
EINDEX