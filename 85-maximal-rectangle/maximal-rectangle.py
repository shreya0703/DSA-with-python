from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def largestRectangleArea(heights: List[int]) -> int:
            n = len(heights)
            st = []
            maxArea = 0

            for i in range(n):
                while st and heights[st[-1]] > heights[i]:
                    element = st.pop()
                    nse = i
                    pse = st[-1] if st else -1
                    width = nse - pse - 1
                    area = heights[element] * width
                    maxArea = max(maxArea, area)
                st.append(i)

            while st:  # Handle remaining bars in stack
                element = st.pop()
                nse = n
                pse = st[-1] if st else -1
                width = nse - pse - 1
                area = heights[element] * width
                maxArea = max(maxArea, area)
            return maxArea

        if not matrix:
            return 0
    
        n, m = len(matrix), len(matrix[0])
    
        # Prefix sum matrix
        psum = [[0] * m for _ in range(n)]
        for j in range(m):
            s = 0
            for i in range(n):
                if matrix[i][j] == "1" or matrix[i][j] == 1:
                    s += 1
                else:
                    s = 0
                psum[i][j] = s

        max_area = 0
        for i in range(n):
            max_area = max(max_area, largestRectangleArea(psum[i]))
    
        return max_area
