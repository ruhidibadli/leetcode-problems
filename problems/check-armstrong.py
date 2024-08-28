import math
def check_armstrong(num: int) -> bool:
    if num <= 0:
        return False
    num = str(num)
    val = len(num)
    sum = 0
    for a in num:
        sum += int(a) ** val 
        if sum > int(num):
            return False 
    if sum == int(num):
        return True      
    else:
        return False
print(check_armstrong(1624))