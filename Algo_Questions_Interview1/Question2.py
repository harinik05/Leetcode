'''
Determine if an integer is prime or not
'''
import math
class Question2:
    def isPrimeOrComposite(self, inputNumber):
        # ending range
        ending = math.sqrt(inputNumber)

        #loop through the entire number
        for i in range(2,int(ending)+1):
            if inputNumber%i == 0:
                print("this is composite")
                return 
        print("this is prime")
        return
    
if __name__=="__main__":
    obj = Question2()
    obj.isPrimeOrComposite(7)

        
