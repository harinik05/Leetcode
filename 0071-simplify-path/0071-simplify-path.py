class Solution:
    def simplifyPath(self, path: str) -> str:
        #1. Initiate a stack 
        stack = []
        
        #2. String.split method 
        splitMethod = path.split("/")
        
        #3. Loop through all of them and put it in a stack 
        for i in range(0, len(splitMethod),1):
            if splitMethod[i] == "..":
                if stack:
                    stack.pop()
            elif splitMethod[i] != "" and splitMethod[i] != ".":
                stack.append(splitMethod[i])
            
        
        #4. concatenate everything in the stack 
        finalStr = "/"+"/".join(stack)
        
        
        #5. return the string
        return finalStr if finalStr else "/"
            
                
        