# Leetcode 155
# Design the stack -> push / pop / top / retrieving
# Minstack Class 
# => void push(int val) / void pop()
# => int top() / int getMin()

class MinStack:

    def __init__(self):
        self.normal = []
        self.only_min = []

    def push(self, val: int) -> None:
        self.normal.append(val)

        if not self.only_min or val < self.only_min[-1]:
            self.only_min.append(val)
        else:
            self.only_min.append(self.only_min[-1])    


    def pop(self) -> None:

        if self.normal:
            self.normal.pop()
            self.only_min.pop()

    def top(self) -> int:

        print(self.normal[-1])
        return self.normal[-1]

    def getMin(self) -> int:

        print(self.only_min[-1])
        return self.only_min[-1]


if __name__ =='__main__':
    calc = MinStack()
    calc.push(-2)
    calc.push(0)
    calc.push(-3)

    calc.getMin()
    calc.pop()
    calc.top()
    calc.getMin()
