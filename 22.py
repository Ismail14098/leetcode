class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        result = []

        def recursion(opened: int, notclosed: int, n:int):
            if len(s) == n*2:
                result.append(''.join(s))
                return
            if opened < n:
                s.append('(')
                recursion(opened+1, notclosed+1, n)
                s.pop()
            if notclosed > 0:
                s.append(')')
                recursion(opened, notclosed-1, n)
                s.pop()
            return

        recursion(0, 0, n)
        return result