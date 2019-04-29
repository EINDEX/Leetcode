# Max Consecutive Ones

## Difficulty
Easy

## Question
<p>Given a binary array, find the maximum number of consecutive 1s in this array.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,1,0,1,1,1]
<b>Output:</b> 3
<b>Explanation:</b> The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
</pre>
</p>

<p><b>Note:</b>
<ul>
<li>The input array will only contain <code>0</code> and <code>1</code>.</li>
<li>The length of input array is a positive integer and will not exceed 10,000</li>
</ul>
</p>

## Solution
### golang
```golang
func findMaxConsecutiveOnes(nums []int) int {
	max := 0
	count := 0
	flag := false

	for _, v := range nums {
		if v == 0 {
			flag = false
		} else {
			if !flag {
				flag = true
				count = 0
			}
			count += 1
			if count > max {
				max = count
			}
		}
	}

	return max
}


```
### python3
```python3
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = 0
        count = 0
        flag = True
        for x in nums:
            if x == 0:
                flag = False
            else:
                if not flag:
                    count = 0
                count += 1
                flag = True
                if count > max_value:
                    max_value = count
        return max_value

```

## Author
EINDEX