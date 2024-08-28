class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vals = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        
        last_opened = []

        for a in s:
            if a in ['(', '[', '{']:
                last_opened.append(a)
            else:    
                if len(last_opened) == 0:
                    return False       
                elif vals[a] != last_opened[-1]:
                    return False
                else:
                    last_opened.pop(-1)
        return len(last_opened) == 0


if __name__ == '__main__':
    sol = Solution()
    res = sol.isValid('(]')
    # res = sol.isValid('([)]')

    print(res)