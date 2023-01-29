import math
def isprime(n):
    cnt = 0
    for i in range(2, n):
        if n % i == 0:
            cnt += 1
    if cnt > 1:
        return False
    else:
        return True

def solution(denum1, num1, denum2, num2):
    a = denum1 * num2 + denum2 * num1
    b = num1 * num2
    if isprime(a) == True or isprime(b) == True:
        return [a, b]
    x = math.gcd(a,b)    
    return [a/x, b/x]