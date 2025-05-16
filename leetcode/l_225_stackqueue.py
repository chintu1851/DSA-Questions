from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # main queue
        self.q2 = deque()  # temp queue

    def push(self, x: int) -> None:
        # Push x into empty q2
        self.q2.append(x)
        # Move all elements from q1 to q2, behind the new element
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap queues so q1 always holds the stack order
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # pop from front of q1, which is top of stack
        return self.q1.popleft()

    def top(self) -> int:
        # return front element of q1 (top of stack) without removing
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Example usage:
if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())   # Output: 2
    print(stack.pop())   # Output: 2
    print(stack.empty()) # Output: False
