
#brackets_1 = ()
#brackets_2 = []
#brackets_3 = {}



class Solution:
    def isValid(self, s:str) -> bool:
        
        brackets_1 = []
        brackets_2 = []
        brackets_3 = []
        
        for item in s:
            if item == "(" or item == ")":
                brackets_1.append(item)
            
            elif item == "[" or item == "]":
                brackets_2.append(item)
                
            elif item == "{" or item == "}": 
                brackets_3.append(item)
        
        if len(brackets_1) % 2 == 0 and len(brackets_2) % 2 == 0 and len(brackets_3) % 2 == 0:
            return True
        else:
            return False


                