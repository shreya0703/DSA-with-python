class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        nge = [-1] * n
        stack = []

        
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                nge[i] = stack[-1]
            stack.append(nums2[i])

        # Get results for nums1
        res = []
        for num in nums1:
            idx = nums2.index(num)
            res.append(nge[idx])
        return res
