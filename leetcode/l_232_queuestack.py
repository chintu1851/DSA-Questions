class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()  # Make sure out_stack has the current front
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


# ✅ Testing the implementation
if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.pop())    # Output: 1
    q.push(3)
    print(q.peek())   # Output: 2
    print(q.pop())    # Output: 2
    print(q.empty())  # Output: False
    print(q.pop())    # Output: 3
    print(q.empty())  # Output: True
