class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def possible(arr, days,m,k):
            count = 0 
            bouquet = 0
            n = len(arr)
            for i in range(n):
                if arr[i]<=days:
                    count +=1
                else:
                    bouquet += count//k
                    count = 0
            bouquet += count//k
            return bouquet>= m 


        n = len(bloomDay)
        if n<m*k:
            return -1
        #mini = float('inf')
        #maxi = float('-inf')
        #for i in range(n):
            #mini = min(mini , bloomDay[i])
            #maxi = max(maxi , bloomDay[i])

        low = min(bloomDay)
        high = max(bloomDay)
        while(low<=high):
            mid = (low+high)//2

            if possible(bloomDay,mid , m , k):
                high = mid-1
            else:
                low = mid+1
        return low

    
        