# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """

#         temp = ""
#         result = ""
#         head = 0
#         for i in range(len(s)):
#             if s[i] not in temp:
#                 temp += s[i]

#                 if i == len(s) - 1:
#                     if len(temp) > len(result):
#                         return len(temp)
#                     else:
#                         return len(result)
#             else:
#                 if len(temp) > len(result):
#                     result = temp
#                 temp = ""
#                 if s[i-1] != s[i]:
#                     temp = s[i-1]
#                 temp += s[i]
                   
#         print(result)
#         return len(result)


# sol = Solution()

# print(sol.lengthOfLongestSubstring("anviaj"))




class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        temp = ""
        result = ""
        con = 0
        head = 0
        while len(s) != 0 or con != len(s):
            if s[con] not in temp:
                temp += s[con]
            else:
                result = temp
            
            temp = ""
            con += 1


sol = Solution()

print(sol.lengthOfLongestSubstring("anviaj"))