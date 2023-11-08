class MinStack:
    q = deque()
    m = deque()
    def __init__(self):
        self.q = deque()
        self.m = deque()
        return

    def push(self, val: int) -> None:
        self.q.append(val)
        if len(self.m)>0:
            el = self.m.pop()
            self.m.append(el)
            self.m.append(min(el, val))
        else:
            self.m.append(val)

    def pop(self) -> None:
        self.q.pop()
        self.m.pop()

    def top(self) -> int:
        el = self.q.pop()
        self.q.append(el)
        return el

    def getMin(self) -> int:
        if len(self.m)==0:
            return 0
        el = self.m.pop()
        self.m.append(el)
        return el