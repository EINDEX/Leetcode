class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 0:
            return 0
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return b
