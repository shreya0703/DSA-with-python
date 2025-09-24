class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sumByD(arr, div):
            total_sum = 0
            for num in arr:
                total_sum += math.ceil(num / div)
            return total_sum

        low = 1
        high = max(nums)

        while low <= high:
            mid = (low + high) // 2
            if sumByD(nums, mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1

        return low

      
        