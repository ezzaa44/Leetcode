class MyQueue:

    def __init__(self):
        self.stack=[]
        self.stack1=[]

    def push(self, x: int) -> None:
        self.stack.append(x)
                   

    def pop(self) -> int:
        if not self.stack1:
            while self.stack:
               self.stack1.append(self.stack.pop())
        return self.stack1.pop()

    def peek(self) -> int:
        if not self.stack1:
            while self.stack:
               self.stack1.append(self.stack.pop())
        return self.stack1[-1]

    def empty(self) -> bool:
        return max(len(self.stack),len(self.stack1))==0