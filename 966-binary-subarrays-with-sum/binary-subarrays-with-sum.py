class Solution:
    def atMost(self, nums, goal):
        if goal < 0:
            return 0
        
        l = 0
        sum_ = 0
        count = 0
        
        for r in range(len(nums)):
            sum_ += nums[r]
            
            while sum_ > goal:
                sum_ -= nums[l]
                l += 1
            
            count += (r - l + 1)
        
        return count
    
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)
