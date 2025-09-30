class MinStack:

    def __init__(self):
        self.st = []
        self.minVal= None
        

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(val)
            self.minVal = val
        elif val >= self.minVal:
            self.st.append(val)
        else:
            self.st.append(2*val - self.minVal)
            self.minVal = val
        

    def pop(self) -> None:
        if not self.st:
            return
        top = self.st.pop()
        if top < self.minVal:
            self.minVal = 2*self.minVal - top

        

    def top(self) -> int:
        if not self.st:
            return None
        top = self.st[-1]
        if top >= self.minVal:
            return top
        else:
            return self.minVal

        

    def getMin(self) -> int:
        return self.minVal

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()