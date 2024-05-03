class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #1. Split and form arrays
        v1Arr = version1.split(".")
        v2Arr = version2.split(".")
        
        # placeholders
        maxLength = max(len(v1Arr), len(v2Arr))
        v1Arr+=['0']*(maxLength-len(v1Arr))
        v2Arr+=['0']*(maxLength-len(v2Arr))
        #2. For loop for all parts of the array
        for i in range(maxLength):
                #a. check if they are equal
                firstVal = int(v1Arr[i])
                secondVal = int(v2Arr[i])
                
                #b. check if its less than 
                if firstVal<secondVal:
                    return -1
                if firstVal > secondVal:
                    return 1
                
        #3. return 0 othervise
        return 0