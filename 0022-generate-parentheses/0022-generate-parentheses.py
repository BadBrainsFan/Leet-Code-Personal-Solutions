class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack (s, open_count, closed_count):
            if len(s) == 2 * n:
                result.append(s)
                return
            if open_count < n:
                backtrack(s + "(", open_count + 1, closed_count)
            if closed_count < open_count:
                backtrack(s + ")", open_count, closed_count + 1)
        result = []
        backtrack("",0,0)
        return result