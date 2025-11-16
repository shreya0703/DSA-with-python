class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hash array of size 256 initialized with -1
        hash_map = [-1] * 256
        l = 0 
        r = 0
        n = len(s)
        max_len = 0

        while r<n:
            char_index = ord(s[r])    # convert char → ASCII index ,ord() is a built-in Python function that returns the ASCII (or Unicode) integer code of a character.
            if hash_map[char_index] != -1:
                if hash_map[char_index] >= l:# if the duplicate index is inside the current window
                     l = hash_map[char_index] + 1 # move left pointer
            hash_map[char_index] = r
            max_len = max(max_len, r - l + 1)
            r+=1
        return max_len

        
        
