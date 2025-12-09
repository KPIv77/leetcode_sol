class Solution:
    def isValid(self, s:str) -> bool:
        
        # Check odd or even
        if len(s) % 2 != 0:
            return False
        
        # loop for check index
        for i in range(len(s) // 2):
            left = s[i]
            right = s[-(i + 1)]
           
        # condition for check 
            if left == "(" and right != ")":
                return False
            elif left == "[" and right != "]":
                return False
            elif left == "{" and right != "}":
                return False
            else:
                return False
           
        return True
    