'''
Given a 16-bit int, create a function to determine if the number of high (1) bits is either
even or odd (i.e. 10101000101 has an odd number of bits)
'''

class Question1:
    def helperFunction(self, inputNum):
        counter = 0
        while inputNum !=0:
            inputNum&=(inputNum-1)
            counter+=1
        
        return counter 
    
    def checkIfEven(self, inputNum):
        if inputNum%2 == 0:
            return True
        else:
            return False
if __name__ == "__main__":
    # Input: 0 --> Output: Number of set bits in 0 is 0 (Even).
    # Input: 1 --> Output: Number of set bits in 1 is 1 (Odd).
    # Input: 2 --> Output: Number of set bits in 2 is 1 (Odd).
    # Input: 5 --> Output: Number of set bits in 5 is 2 (Even).
    # Input: 10 --> Output: Number of set bits in 10 is 2 (Even).
    # Input: 15 --> Output: Number of set bits in 15 is 4 (Even).
    # Input: 30 --> Output: Number of set bits in 30 is 4 (Even).
    # Input: 65535 --> Output: Number of set bits in 65535 is 16 (Even).

    objInstance = Question1()
    result = objInstance.helperFunction(65535)
    print(result)
    boolCheck = objInstance.checkIfEven(result)
    print(boolCheck)
