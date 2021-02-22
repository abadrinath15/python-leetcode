class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        if not self.data or x < self.getMin():
            self.data.append((x, x))
        else:
            self.data.append((x, self.getMin()))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]
