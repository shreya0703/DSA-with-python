class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Frequency map of characters in t
        freq = {}
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1

        required = len(t)      # how many chars we still need
        l = 0
        minLen = float("inf")
        startIndex = -1

        # Sliding window
        for r in range(len(s)):

            if s[r] in freq:
                freq[s[r]] -= 1
                if freq[s[r]] >= 0:
                    required -= 1

            # when window is valid → shrink
            while required == 0:
                # update minimum window
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    startIndex = l

                # shrink from left
                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] > 0:
                        required += 1

                l += 1

        if startIndex == -1:
            return ""

        return s[startIndex : startIndex + minLen]
