# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l < h:
            m = l + (h - l) // 2
            if not isBadVersion(m):
                l = m + 1
            else:
                h = m
        
        return l
        