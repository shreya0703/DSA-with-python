class Solution:
    def atMostK(self, nums, K):
        freq = {}
        left = 0
        count = 0

        for right in range(len(nums)):
            if nums[right] not in freq or freq[nums[right]] == 0:
                K -= 1
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while K < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    K += 1
                left += 1

            count += (right - left + 1)

        return count

    def subarraysWithKDistinct(self, nums, k):
        # exactly k = atMost(k) - atMost(k-1)
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)
