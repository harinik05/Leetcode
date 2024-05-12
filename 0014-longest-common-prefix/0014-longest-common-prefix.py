from typing import List

class Solution:
    def findCommonPrefix(self, string1, string2):
        outputStr = ""
        minLen = min(len(string1), len(string2))
        for i in range(minLen):
            if string1[i] == string2[i]:
                outputStr += string1[i]
            else:
                break
        return outputStr
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        commonPrefix = strs[0]
        for string in strs[1:]:
            commonPrefix = self.findCommonPrefix(commonPrefix, string)
            if not commonPrefix:
                break
        
        return commonPrefix
