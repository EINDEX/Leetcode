# Guess Number Higher or Lower

## Difficulty
Easy

## Question
<p>We are playing the Guess Game. The game is as follows:</p>

<p>I pick a number from <b>1</b> to <b><i>n</i></b>. You have to guess which number I picked.</p>

<p>Every time you guess wrong, I&#39;ll tell you whether the number is higher or lower.</p>

<p>You call a pre-defined API <code>guess(int num)</code> which returns 3 possible results (<code>-1</code>, <code>1</code>, or <code>0</code>):</p>

<pre>
-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
</pre>

<p><strong>Example :</strong></p>

<div>
<pre>
<strong>Input: </strong>n = <span id="example-input-1-1">10</span>, pick = <span id="example-input-1-2">6</span>
<strong>Output: </strong><span id="example-output-1">6</span>
</pre>
</div>


## Solution
### java
```java
/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int L=1,R=n;
        int res=0;
        while(L<=R){
            int mid= R-((R-L)>>1);
            res=guess(mid);
            if(res==0)return mid;
            else if(res==1)L=mid+1;
            else R=mid-1;
        }
        return L;
    }
}
```
### python
```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        L=1
        R=n
        res=0
        while L<=R:
            mid= R-((R-L)>>1)
            res=guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                L=mid+1
            else:
                R=mid-1
        return L


```

## Author
EINDEX