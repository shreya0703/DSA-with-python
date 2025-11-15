class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = 0
        max_len = 0

        for r, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= l:
                l = last_seen[ch] + 1

            last_seen[ch] = r
            max_len = max(max_len, r - l + 1)

        return max_len
        
