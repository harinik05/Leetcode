class Solution(object):
    def reversePrefix(self, word, ch):
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
        