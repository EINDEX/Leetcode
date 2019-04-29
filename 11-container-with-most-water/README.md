# Container With Most Water

## Difficulty
Medium

## Question
<p>Given <i>n</i> non-negative integers <i>a<sub>1</sub></i>, <i>a<sub>2</sub></i>, ..., <i>a<sub>n&nbsp;</sub></i>, where each represents a point at coordinate (<i>i</i>, <i>a<sub>i</sub></i>). <i>n</i> vertical lines are drawn such that the two endpoints of line <i>i</i> is at (<i>i</i>, <i>a<sub>i</sub></i>) and (<i>i</i>, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.</p>

<p><strong>Note:&nbsp;</strong>You may not slant the container and <i>n</i> is at least 2.</p>

<p>&nbsp;</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;" /></p>

<p><small>The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain&nbsp;is 49. </small></p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49</pre>


## Solution
### python
```python
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        m = 0
        while i < j:
            h = min(height[i], height[j])
            s = h * (j - i)
            if s > m:
                m = s
            while height[i] <= h and i < j:
                i += 1
            while height[j] <= h and i < j:
                j -= 1
        return m
        

```
### python3
```python3
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        m = 0
        while i < j:
            h = min(height[i], height[j])
            s = h * (j - i)
            if s > m:
                m = s
            while height[i] <= h and i < j:
                i += 1
            while height[j] <= h and i < j:
                j -= 1
        return m
        
```

## Author
EINDEX