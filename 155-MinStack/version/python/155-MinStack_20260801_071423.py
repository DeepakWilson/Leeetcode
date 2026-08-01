# Last updated: 8/1/2026, 7:14:23 AM
1class MinStack:
2    def __init__(self):
3        self.stk=[]
4        self.minstk=[]     
5    def push(self, value: int) -> None:
6        self.stk.append(value)    
7        if not self.minstk:
8            self.minstk.append(value)
9        elif self.minstk[-1] < value:
10            self.minstk.append(self.minstk[-1])
11        else:
12            self.minstk.append(value)
13    def pop(self) -> None:
14        self.stk.pop()       
15        self.minstk.pop() 
16    def top(self) -> int:
17        return self.stk[-1]
18    def getMin(self) -> int:
19        return self.minstk[-1]