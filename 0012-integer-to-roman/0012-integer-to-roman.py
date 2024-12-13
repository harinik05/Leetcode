class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return ""
        # Define a hashmap first with this set of symbols and their numbers 
        mainHM = []
        mainHM.append((1000, 'M'))
        mainHM.append((900, 'CM'))
        mainHM.append((500, 'D'))
        mainHM.append((400, 'CD'))
        mainHM.append((100, 'C'))
        mainHM.append((90, 'XC'))
        mainHM.append((50, 'L'))
        mainHM.append((40, 'XL'))
        mainHM.append((10, 'X'))
        mainHM.append((9, 'IX'))
        mainHM.append((5, 'V'))
        mainHM.append((4, 'IV'))
        mainHM.append((1, 'I'))
     
        
        # Go through everything in the hashmap divide by this 
        finalAnswer = ""
        
        # Loop through all elements of the hashmap 
        for key, value in mainHM:
            # Divide the number by value 
            divisionAnswer = num // key
            
            # Find the modulo (remainder)
            remainder = num % key
            
            # Put the division answer * value which was the symbol 
            num = remainder 
            finalAnswer += (divisionAnswer * value)
        
        return finalAnswer
        
        