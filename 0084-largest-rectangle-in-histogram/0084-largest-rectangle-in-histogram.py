class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []
        for index,height in enumerate(heights+[0]):
            while stack and height<=heights[stack[-1]]:
                H = heights[stack.pop()]
                W = index if not stack else index-stack[-1]-1
                area = max(area, W*H)
            stack.append(index)
        return area