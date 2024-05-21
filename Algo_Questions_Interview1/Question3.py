class Question3:
    def flattenArrayFunction(self, inputArr):
        #1. Initialize the variables to return 
        flatArr = []
        stack = inputArr[:]

        #2. Loop through the entire stack 
        while stack:
            elementPop = stack.pop()
            if isinstance(elementPop, list):
                stack.extend(elementPop)
            else:
                flatArr.append(elementPop)
        return flatArr[::-1]
    
if __name__ == "__main__":
    obj = Question3()
    inputArr = [1, 2, [[3], [4, 5], [], 6], 7, [[[8]]]]
    outputArr= obj.flattenArrayFunction(inputArr)
    print(outputArr)