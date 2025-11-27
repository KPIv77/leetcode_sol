"""
Step1 define value in str(I = 1, V = 5, etc...).
step2 check input.
      create condition and loop for read each element and len of input.
        if len(input) == 1
            print(input)
        else:
            to stap3
step3 treat input as words and spilt each element for put in list. 
step4 analys pattern roman number if current index more >= next index sum both index 
      if < next index minus both 
step5 create condition and loop for anlys and return in list[]
step6 sum(list[]) 
"""

class Solution:
    
    def romanToInt(self, s:str) -> int:

        roman_num = ["I", "V", "X", "L", "C", "D", "M"]         
        num = [1, 5, 10, 50, 100, 500, 1000]
        
        dict_roman = dict(zip(roman_num, num))
        real_num = []
        sum_realnum = []
         
        if len(s) == 1:
            return (dict_roman[s])  

        elif len(s) != 1:
            for index in range(len(s)):
                real_num.append(dict_roman[str(s[index])])

        for item in range(len(real_num)):
            
            if item + 1 < len(real_num):
                
                if real_num[item] >= real_num[item + 1]:
                    sum_realnum.append(real_num[item])
                else:
                    sum_realnum.append(-real_num[item])
            else:
                sum_realnum.append(real_num[-1])
            
        
        return sum(sum_realnum) 

