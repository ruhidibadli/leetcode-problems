### math.gcd metodu kullanilarak direkt cozulebilir

import time
class Solution:
    def find_gcd(self, num1: int, num2: int) -> int:
        cd1 = []
        cd2 = []

        for a in range(1, num1+1):
            if num1 % a == 0:
                cd1.append(a) 
        for b in range(1, num2+1):
            if num2 % b == 0:
                cd2.append(b) 
        print(cd1)
        print(cd2)

        gcd = max(set(cd1).intersection(cd2))
        return gcd

if __name__ == '__main__':

    start = time.monotonic()   
    sol = Solution()


    print(sol.find_gcd(10000, 1000000))

    end = time.monotonic()

    print(f'time: {end - start}')