"""
step1 check type list, empty list or non-empty list
step2 check prefix in list by list[0] as a reference.

"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for word in strs[1:]:
            
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                
        return prefix
                             


