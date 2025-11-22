class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def atMost(x):
            if x < 0:
                return 0
            
            l = 0
            odd = 0
            count = 0
            
            for r in range(len(nums)):
                odd += nums[r] % 2     # count odd numbers
                
                while odd > x:
                    odd -= nums[l] % 2
                    l += 1
                
                count += (r - l + 1)
            
            return count
        
        return atMost(k) - atMost(k - 1)
