# Shuffle an Array

## Difficulty
Medium

## Question
<p>Shuffle a set of numbers without duplicates.
</p>

<p><b>Example:</b>
<pre>
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
</pre>
</p>

## Solution
### python
```python
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums[:]
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        random.shuffle(self.nums)
        return self.nums


```
### python3
```python3
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums[:]
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        random.shuffle(self.nums)
        return self.nums

```

## Author
EINDEX