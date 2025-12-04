
"""
step1 check even or odd  


"""



class Solution:
    def isValid(self, s:str) -> bool:
       
        if len(s) % 2 != 0:
            return False
       
        for i in range(len(s) // 2):
            left = s[i]
            right = s[-(i + 1)]
           
            if left == "(" and right != ")":
                return False
            elif left == "[" and right != "]":
                return False
            elif left == "{" and right != "}":
                return False
            elif left not in "([{":
                return False
           
        return True
    