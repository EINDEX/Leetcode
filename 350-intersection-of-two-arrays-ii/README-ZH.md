# Intersection of Two Arrays II

## Difficulty
Easy

## Question
<p>Given two arrays, write a function to compute their intersection.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums1 = <span id="example-input-1-1">[1,2,2,1]</span>, nums2 = <span id="example-input-1-2">[2,2]</span>
<strong>Output: </strong><span id="example-output-1">[2,2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums1 = <span id="example-input-2-1">[4,9,5]</span>, nums2 = <span id="example-input-2-2">[9,4,9,8,4]</span>
<strong>Output: </strong><span id="example-output-2">[4,9]</span></pre>
</div>

<p><b>Note:</b></p>

<ul>
	<li>Each element in the result should appear as many times as it shows in both arrays.</li>
	<li>The result can be in any order.</li>
</ul>

<p><b>Follow up:</b></p>

<ul>
	<li>What if the given array is already sorted? How would you optimize your algorithm?</li>
	<li>What if <i>nums1</i>&#39;s size is small compared to <i>nums2</i>&#39;s size? Which algorithm is better?</li>
	<li>What if elements of <i>nums2</i> are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?</li>
</ul>


## Solution
### python
```python
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        
        data = {}
        for x in nums1:
            data.setdefault(x,0)
            data[x] += 1
        
        res = []
        for x in nums2:
            if x in data and data[x]>0:
                data[x]-=1
                res.append(x)
                
        return res


```
### python3
```python3
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        
        data = {}
        for x in nums1:
            data.setdefault(x,0)
            data[x] += 1
        
        res = []
        for x in nums2:
            if x in data and data[x]>0:
                data[x]-=1
                res.append(x)
                
        return res
```

## Author
EINDEX