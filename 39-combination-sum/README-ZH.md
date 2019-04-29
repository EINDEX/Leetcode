# Combination Sum

## Difficulty
Medium

## Question
<p>Given a <strong>set</strong> of candidate numbers (<code>candidates</code>) <strong>(without duplicates)</strong> and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sums to <code>target</code>.</p>

<p>The <strong>same</strong> repeated number may be chosen from <code>candidates</code>&nbsp;unlimited number of times.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All numbers (including <code>target</code>) will be positive integers.</li>
	<li>The solution set must not contain duplicate combinations.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = <code>[2,3,6,7], </code>target = <code>7</code>,
<strong>A solution set is:</strong>
[
  [7],
  [2,2,3]
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,5]<code>, </code>target = 8,
<strong>A solution set is:</strong>
[
&nbsp; [2,2,2,2],
&nbsp; [2,3,3],
&nbsp; [3,5]
]
</pre>


## Solution
### python
```python
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def inner(nums,low_value, candidates, target):
            if target == 0:
                res.append(nums)
            elif target < low_value:
                return
            for x in candidates:
                if x >= low_value:
                    inner(nums+[x],x, candidates, target-x)
        inner([],0, candidates, target)
        return res
        

```
### python3
```python3
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def inner(nums,low_value, candidates, target):
            if target == 0:
                res.append(nums)
            elif target < 0:
                return
            for x in candidates:
                if x >= low_value:
                    inner(nums+[x],x, candidates, target-x)
        inner([],0, candidates, target)
        return res
        
```

## Author
EINDEX