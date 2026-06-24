from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_str = ""
        for s in strs:
            # Prefix each string with its length and a '#' delimiter
            encoded_str += f"{len(s)}#{s}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        
        while i < len(s):
            # 1. Find the delimiter to isolate the length prefix
            j = i
            while s[j] != '#':
                j += 1
            
            # 2. Extract the length integer
            length = int(s[i:j])
            
            # 3. Slice the actual string based on that length
            start_of_str = j + 1
            end_of_str = start_of_str + length
            res.append(s[start_of_str:end_of_str])
            
            # 4. Move the pointer to the start of the next encoded block
            i = end_of_str
            
        return res