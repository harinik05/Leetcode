from typing import List 

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        returnSet = set()
        counter = 0
        for email in emails:
            #1. Determine the local and domain name 
            local, domain = email.split("@")
            
            #2. Check if there is a . then just remove it 
            '''
            if "." in local:
                dots = local.split(".")
                local = "".join(dots)
            '''
            #2 alternative)  replacement 
            if "." in local:
                local = local.replace(".","")
            
            #3. Check if there is a + sign then ignore the rest 
            if "+" in local:
                plus = local.split("+")
                local = plus[0]
            
            #4. Once filtering is done put it in a set
            fullEmail = f"{local}@{domain}"
            returnSet.add(fullEmail)
            
        
        return len(returnSet) 
        