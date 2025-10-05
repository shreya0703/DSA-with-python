class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        maxArea = 0

        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                element = st.pop()
                nse = i
                pse = st[-1] if st else -1
                width = nse - pse -1
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


        