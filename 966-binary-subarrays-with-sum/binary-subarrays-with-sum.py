class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def atMost(k):
            if k < 0:
                return 0
            
            l = 0
            sum_ = 0
            count = 0
            
            for r in range(len(nums)):
                sum_ += nums[r]
                
                while sum_ > k:
                    sum_ -= nums[l]
                    l += 1
                
                count += (r - l + 1)
            
            return count
        
        return atMost(goal) - atMost(goal - 1)
