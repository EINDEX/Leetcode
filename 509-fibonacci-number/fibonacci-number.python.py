class Solution:
    
    
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        a, b = 0, 1
        for _ in range(N-1):
            a, b = b, a+b
        return b
            
        
