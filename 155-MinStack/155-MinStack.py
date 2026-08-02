# Last updated: 8/2/2026, 7:11:00 PM
class MinStack:
    def __init__(self):
        self.stk=[]
        self.minstk=[]     
    def push(self, value: int) -> None:
        self.stk.append(value)    
        if not self.minstk:
            self.minstk.append(value)
        elif self.minstk[-1] < value:
            self.minstk.append(self.minstk[-1])
        else:
            self.minstk.append(value)
    def pop(self) -> None:
        self.stk.pop()       
        self.minstk.pop() 
    def top(self) -> int:
        return self.stk[-1]
    def getMin(self) -> int:
        return self.minstk[-1]