class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        for i in range(n):
            # compare current with next (using modulo for circular check)
            if nums[i] > nums[(i + 1) % n]:
                count += 1

        # valid if there is at most one "drop"
        return count <= 1
    
        