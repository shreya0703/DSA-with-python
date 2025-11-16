class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}       # stores last seen index of each character
        l = 0                # left pointer of window
        max_len = 0

        for r, ch in enumerate(s):
            # If character repeated inside the window, move left pointer
            if ch in last_seen and last_seen[ch] >= l:
                l = last_seen[ch] + 1

            # Update last seen index of the character
            last_seen[ch] = r

            # Update max window length
            max_len = max(max_len, r - l + 1)

        return max_len
