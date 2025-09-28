class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def maxElement(mat,col):
            n = len(mat)
            max_value = float('-inf')
            index = -1
            for i in range(n):
                if mat[i][col]>= max_value:
                    max_value = mat[i][col]
                    index = i
            return index

        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m-1
        while(low<=high):
            mid = (low+high)//2
            row = maxElement(mat,mid)
            left = mat[row][mid-1] if (mid-1)>0 else -1
            right = mat[row][mid+1] if (mid+1) <m  else  -1
            if mat[row][mid]> left and mat[row][mid] > right:
                return row, mid
            elif left > mat[row][mid]:
                high = mid -1
            else:
                low = mid +1
        return [-1,-1]  