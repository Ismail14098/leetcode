class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = deque()
        for token in tokens:
            if token == '+':
                q.append(q.pop() + q.pop())
            elif token == '-':
                el2, el1 = q.pop(), q.pop()
                q.append(el1 - el2)
            elif token == '*':
                el2, el1 = q.pop(), q.pop()
                q.append(el1 * el2)
            elif token == '/':
                el2, el1 = q.pop(), q.pop()
                q.append(int(el1 / el2))
            else:
                q.append(int(token))
        return q.pop()