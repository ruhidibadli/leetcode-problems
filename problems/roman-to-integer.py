class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        datas = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        num = 0
        for i in range(len(s)):
            if i < len(s) - 1 and datas[s[i]] < datas[s[i+1]]:
                num -= datas[s[i]]
            else:
                num += datas[s[i]]
            
        return num
    
sol = Solution()
print(sol.romanToInt('MCMXCIV'))