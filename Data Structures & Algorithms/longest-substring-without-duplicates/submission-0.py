class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()       # To store unique characters
        left = 0               # Left pointer of the sliding window
        max_len = 0            # Track max length

        for right in range(len(s)):
            while s[right] in char_set:
                # Remove from the left until s[right] becomes unique
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len
