class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            x = x[1::1]
            x = f'-{x[::-1]}'
        else:
            x = x[::-1]
        
        x = int(x)
        if not -pow(2, 31) <= x <= pow(2, 31): 
            return 0
        return x



if __name__ == '__main__':
    sol = Solution()

    print(sol.reverse(1534236469))