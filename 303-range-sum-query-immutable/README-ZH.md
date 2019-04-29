# Range Sum Query - Immutable

## Difficulty
Easy

## Question
<p>Given an integer array <i>nums</i>, find the sum of the elements between indices <i>i</i> and <i>j</i> (<i>i</i> &le; <i>j</i>), inclusive.</p>

<p><b>Example:</b><br>
<pre>
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>You may assume that the array does not change.</li>
<li>There are many calls to <i>sumRange</i> function.</li>
</ol>
</p>

## Solution
### python3
```python3
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.results = []
        if not nums:
            return
        self.results.append(nums[0])
        for x in range(1, len(nums)):
            self.results.append(self.results[x-1]+nums[x])
            

    def sumRange(self, i: int, j: int) -> int:
        if i <= 0:
            m = 0
        else:
            m = self.results[i-1]
        
        return self.results[j] - m


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
```

## Author
EINDEX