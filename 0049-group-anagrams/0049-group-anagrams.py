from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #1. Initialize the hashmap: values will be empty lists
        finalHashmap = defaultdict(list)
        
        #2. Loop through the list and sort
        for words in strs:
            sortedWord = ''.join(sorted(words))
            finalHashmap[sortedWord].append(words)
        
        resultArr = []
        #3. Loop through the hashmap to produce the final result
        for values in finalHashmap.values():
            resultArr.append(values)
        return resultArr
        
        
        
        