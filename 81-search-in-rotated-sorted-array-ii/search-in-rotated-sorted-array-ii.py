class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            # Handle duplicates
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # Left half sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False