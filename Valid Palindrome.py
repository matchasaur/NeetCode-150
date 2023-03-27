class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Regex solution
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        print(s)
        i = 0
        j = len(s)-1
        while (not(i > j)):
            if (s[i] != s[j]):
                return False
            i += 1
            j -= 1
        return True
