class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        #1. Convert into a list 
        wordList = list(word)
        outputWord = ""
        
        #2. determine the index where ch is there
        try:
            indexPresent = wordList.index(ch)
        except ValueError:
            return word
        
        #3. check if you can find out to reverse it
        if indexPresent!=-1:
            outputWord = ''.join(reversed(wordList[0:indexPresent+1]))
            outputWord += ''.join(wordList[indexPresent+1:])
        
        #4. return the output word
        return outputWord
    '''
    class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        #1. Initialize the return string
        returnStr= word

        #2. Reverse the string
        for i in range(len(word)):
            if word[i] == ch:
                returnStr = ''.join(reversed(word[0:i+1]))
                returnStr = returnStr+word[i+1:]
                return returnStr

        #3. return the final answer
        return returnStr
    '''