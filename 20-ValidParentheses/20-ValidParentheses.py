# Last updated: 6/18/2026, 7:04:45 PM
class Solution(object):
    def isValid(self, s):
        stack =[]
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                stack.append(ch)
            elif ch==')':
                if not stack or stack.pop()!='(':
                    return False
            elif ch=='}':
                if not stack or stack.pop()!='{':
                    return False
            elif ch==']':
                if not stack or stack.pop()!='[':
                    return False
        return len(stack) == 0
