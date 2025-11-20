class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        count = 0
        freq = {0: 0}
        freq[0] = 1   # one way to have prefix sum 0 before starting

        for num in nums:
            prefix += num

            # we need prefix - goal seen before
            if prefix - goal in freq:
                count += freq[prefix - goal]

            # store current prefix
            freq[prefix] = freq.get(prefix, 0) + 1

        return count
