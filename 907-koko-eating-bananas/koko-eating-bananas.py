import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findmax(plies):
            maxi = float(-inf)
            n = len(piles)
            for i in range(n):
                maxi = max(maxi , piles[i])
            return maxi
        def calculateTotalHours(piles,hourly):
            totalH = 0
            n = len(piles)
            for i in range(n):
                totalH += math.ceil(piles[i]/hourly)

            return totalH
        
        low = 1
        high = findmax(piles)
        while(low <= high):
            mid = (low+high)//2
            totalHours = calculateTotalHours(piles,mid)
            if totalHours<= h :
                high = mid - 1
            else:
                low = mid +1
        return low


        
        