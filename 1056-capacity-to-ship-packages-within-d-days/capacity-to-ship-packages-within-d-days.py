class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def noOfDays(weight,cap):
            days = 1 # first day
            load = 0
            n = len(weight)
            for i in range(n):
                if(load + weight[i]>cap):
                    days = days+1 # next day
                    load = weight[i] # load that weight
                else:
                    load += weight[i]  # add load in same day
            return days

        low = max(weights)
        high = sum(weights)
        while(low<=high):
            mid = (low+high)//2
            no_of_days = noOfDays(weights,mid)
            if no_of_days <= days:
                high = mid -1
            else:
                low = mid +1
        return low

        