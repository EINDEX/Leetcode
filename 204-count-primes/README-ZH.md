# Count Primes

## Difficulty
Easy

## Question
<p>Count the number of prime numbers less than a non-negative number, <b><i>n</i></b>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
</pre>


## Solution
### python
```python
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        res = [True]*n
        res[0], res[1] = False, False
        
        for i in range(2, n):
            if i * i >= n:
                break
                
            if not res[i]:
                continue
            
            for j in range(i*i, n, i):
                res[j] = False
        
        return sum(res)
                        
        

```
### python3
```python3
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        res = [True]*n
        res[0], res[1] = False, False
        
        for i in range(2, n):
            if i * i >= n:
                break
                
            if not res[i]:
                continue
            
            for j in range(i*i, n, i):
                res[j] = False
        
        return sum(res)
                        
        
```

## Author
EINDEX