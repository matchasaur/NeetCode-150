class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False
        
        x = []
        y = []
        x[:0] = s
        y[:0] = t

        x.sort()
        y.sort()

        return x == y 
