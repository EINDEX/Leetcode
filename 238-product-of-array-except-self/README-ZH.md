# Product of Array Except Self

## Difficulty
Medium

## Question
<p>Given an array <code>nums</code> of <em>n</em> integers where <em>n</em> &gt; 1, &nbsp;return an array <code>output</code> such that <code>output[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code>.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b>  <code>[1,2,3,4]</code>
<b>Output:</b> <code>[24,12,8,6]</code>
</pre>

<p><strong>Note: </strong>Please solve it <strong>without division</strong> and in O(<em>n</em>).</p>

<p><strong>Follow up:</strong><br />
Could you solve it with constant space complexity? (The output array <strong>does not</strong> count as extra space for the purpose of space complexity analysis.)</p>


## Solution
### python
```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 1
        zeros = 0
        index = None
        for i,n in enumerate(nums):
            if n == 0:
                zeros +=1
                index = i
            else:
                res *= n
        if zeros >=2:
            return [0]*len(nums)
        elif zeros == 1:
            l = [0]*len(nums)
            l[index] = res
            return l
        return [res/s for s in nums]

```

## Author
EINDEX