class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while(True):
                if len(stack) == 0:
                    stack.append((temp, i))
                    break
                el, j = stack.pop()
                if el >= temp:
                    stack.append((el, j))
                    stack.append((temp, i))
                    break
                else:
                    answer[j] = i-j
        return answer

# Improved
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                el, j = stack.pop()
                answer[j] = i-j
            stack.append((temp, i))
        return answer