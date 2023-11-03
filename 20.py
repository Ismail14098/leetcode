class Solution:
    op = {'(', '[', '{'}
    close = {')': '(', ']': '[', '}': '{'}
    def isValid(self, s: str) -> bool:
        stack = deque()
        for el in s:
            if el in self.op:
                stack.append(el)
            elif len(stack) != 0:
                pair = self.close[el]
                last = stack.pop()
                if pair != last:
                    return False
            else:
                return False
        return len(stack) == 0