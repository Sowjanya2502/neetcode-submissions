class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            index=i
            while stack and stack[-1][0]>heights[i]:
                height,index = stack.pop()
                max_area=max(max_area, height*(i-index))
            stack.append((heights[i],index))
        for h,i in stack:
            max_area = max(max_area, h*(len(heights)-i))
        return max_area
