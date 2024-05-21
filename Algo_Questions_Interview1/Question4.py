'''
Valid IPv4 address strings contain four, period delimited segments. Each segment
contains [0, 3] characters that represent a number in the range [0, 255]. The number must
not have leading zeroes.
a. Valid example: 255.123.0.88
b. Invalid example: 0,55.abc.1434
c. Given a string of alphanumeric characters, write a function to determine if the
string represents a valid IPv4 address.
'''
class Question4:
    def isValidAddress(self, inputString):
        # Segmented Array 
        segArr = inputString.split(".")
        if len(segArr) !=4:
            return False
        
        # Check each of the elements in the array
        for elements in segArr:
            #1. Check that the element doesnt have any leading 0s
            if elements[0] == '0' and len(elements)>1:
                return False
            
            #2. Check if there is between 0 and 3
            elif not(len(elements)>=0 and len(elements)<=3):
                return False

            #3. check if the elements has a value between 0 and 255
            try:
                num = int(elements)
                if not 0<=num<=255:
                    return False
            except ValueError:
                return False
        
        return True
    
if __name__=="__main__":
    obj = Question4()
    print(obj.isValidAddress("0,55.abc.1434"))
