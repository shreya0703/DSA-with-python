class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lb(arr, x):
            n = len(arr)
            low = 0
            high = n-1
            ans = n
            while(low<=high):
                mid = (low + high)//2
                if nums[mid]>=x:
                    ans = mid
                    high = mid -1
                else:
                    low = mid +1
            return ans

        def ub(arr, x):
            n = len(arr)
            low = 0
            high = n-1
            ans = n
            while(low<=high):
                mid = (low + high)//2
                if (nums[mid]>x):
                    ans = mid
                    high = mid -1 
                else:
                    low= mid +1
            return ans

        left = lb(nums,target)
        right = ub(nums, target) -1

        if left <= right and left<len(nums) and nums[left] == target and nums[right] == target:
            return[left, right]
        else:
            return[-1,-1]

        