class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #0. result initialization 
        array = []
        #1. Find all the elements in this array
        for i in range(1,n+1,1):
            if i%3==0 and i%5==0:
                array.append("FizzBuzz")
            elif i%3==0:
                array.append("Fizz")
            elif i%5==0:
                array.append("Buzz")
            else:
                array.append(str(i))
        
        return array
            