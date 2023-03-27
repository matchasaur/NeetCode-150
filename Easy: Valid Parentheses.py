#Original Solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        myStack = deque()
        temp = ""
        for char in s:
            if(len(myStack)!=0):
                topStack = myStack.pop()
            else:
                myStack.append(char)
                continue
            temp = topStack + char
            if (temp == "()" or temp == "[]" or temp == "{}"):
                continue
            else:
                myStack.append(topStack)
                myStack.append(char)

        if (len(myStack)==0):
            return True
        return False

#Better solution
class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
