


class Solution:
    def isValid(self, s:str) -> bool:
        
        
        for index_s in range(len(s)):
            if s[index_s] == "(" and s[-(index_s+1)] == ")":
                return True 
            elif s[index_s] == "[" and s[-(index_s+1)] == "]":
                return True
            elif s[index_s] == "{" and s[-(index_s+1)] == "}":
                return True 
            elif s[index_s] == "(" and s[-(index_s+1)] != ")":
                return False
            elif s[index_s] == "[" and s[-(index_s+1)] != "]":
                return False
            elif s[index_s] == "{" and s[-(index_s+1)] != "}":
                return False



           
          
s = Solution()
print(s.isValid("((((()))))"))                          
