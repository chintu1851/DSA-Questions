class MinStack:

    def __init__(self):
        self.stack=[]
        self.tempstack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.tempstack[-1] if self.tempstack else val)
        self.tempstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.tempstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.tempstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()