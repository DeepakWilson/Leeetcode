# Last updated: 8/1/2026, 8:57:32 AM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack=[]
4        for c in tokens:
5            if c=="+":
6                stack.append(stack.pop() + stack.pop())
7            elif c=="-":
8                a,b=stack.pop(),stack.pop()
9                stack.append(b-a)
10            elif c=="*":
11                stack.append(stack.pop()*stack.pop())
12            elif c=="/":
13                a,b=stack.pop(),stack.pop()
14                stack.append(int(b/a))
15            else:
16                stack.append(int(c))
17        return stack[0]