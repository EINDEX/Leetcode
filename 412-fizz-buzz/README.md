# Fizz Buzz

## Difficulty
Easy

## Question
<p>Write a program that outputs the string representation of numbers from 1 to <i>n</i>.</p>

<p>But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.</p>

<p><b>Example:</b>
<pre>
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
</pre>
</p>

## Solution
### python
```python
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for x in range(1, n+1):
            if x % 15 == 0:
                res.append("FizzBuzz")
            elif x % 5 == 0:
                res.append("Buzz")
            elif x % 3 == 0:
                res.append("Fizz")
            else:
                res.append(str(x))
            
            
        return res


```
### python3
```python3
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for x in range(1, n+1):
            if x % 15 == 0:
                res.append("FizzBuzz")
            elif x % 5 == 0:
                res.append("Buzz")
            elif x % 3 == 0:
                res.append("Fizz")
            else:
                res.append(str(x))
            
            
        return res
```

## Author
EINDEX