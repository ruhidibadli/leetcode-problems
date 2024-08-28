class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        prefix = []
        last_index = 0
        b = False
        prefix = list(strs[0])
        for index, obj in enumerate(prefix):
            for i in strs[1:]:
                try:
                    if not i[index] == obj:
                        b = True
                except IndexError:
                    b = True
            if b:
                break
            last_index += 1
        if last_index == 0:
            return ''
        prefix = ''.join(prefix[:last_index])
        return prefix
        
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ## BEST SOLVE
        ans=""
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 


if __name__ == '__main__':
    sol = Solution()
    result = sol.longestCommonPrefix(['ab', 'a'])
    # result = sol.longestCommonPrefix(['dog', 'racecar', 'car'])

    # result = sol.longestCommonPrefix(['flower', 'flow', 'flight'])
    print(result)