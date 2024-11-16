class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for right in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[right]:
                left = stack.pop()
                answer[left] = right - left
            stack.append(right)
        return answer