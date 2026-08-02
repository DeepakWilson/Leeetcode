# Last updated: 8/2/2026, 7:11:03 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c=="+":
                stack.append(stack.pop() + stack.pop())
            elif c=="-":
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif c=="*":
                stack.append(stack.pop()*stack.pop())
            elif c=="/":
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]