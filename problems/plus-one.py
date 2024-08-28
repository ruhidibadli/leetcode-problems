class Solution:
    def plusOne(self, digits: list) -> list:
        a = len(digits)
        con = 1
        while a > 0:
            if con == 0:
                return digits
            if digits[a-1] == 9:
                digits[a-1] = 0
            else:
                digits[a-1] += 1
                con = 0
            a -= 1
        if a == 0 and con == 1:
            return [1] + digits
        else:
            return digits
if __name__ == '__main__':
    sol = Solution()

    res = sol.plusOne([8, 9 ,9])
    print(res)