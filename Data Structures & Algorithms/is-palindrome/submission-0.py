class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Clean the string: keep only alphanumeric chars and lowercase them
        cleaned = [char.lower() for char in s if char.isalnum()]
        
        # 2. Run the two-pointer check on the cleaned list
        l = 0
        r = len(cleaned) - 1
        
        while l < r:
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1
            
        return True