# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


class MinStack:

    def __init__(self):
        

    def push(self, val: int) -> None:
        if not self.minimum_stack or self.minimum_stack[-1] >= val:
            self.minimum_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.minimum_stack[-1] == self.stack[-1]:
            self.minimum_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()