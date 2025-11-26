class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        i = len(s) - 1   # Start from the end
        
        while i >= 0:
            
            # 1. Skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1
            
            if i < 0:
                break
            
            # 2. Mark the end of the word
            end = i
            
            # 3. Move left until space -> this gives start of word
            while i >= 0 and s[i] != " ":
                i -= 1
            
            # 4. Extract word (no split used)
            word = s[i + 1 : end + 1]
            
            # 5. Add space if needed
            if result != "":
                result += " "
            
            # 6. Append the current word
            result += word
        
        return result