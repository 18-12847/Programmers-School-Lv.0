def isprime(a):
    cnt = 0
    for i in range(1, a+1):
        if a % i == 0:
            cnt += 1
    if cnt <= 2:
        return True
    else:
        return False
        
def solution(n):
    ans = []
    if isprime(n):
        ans.append(n)
        return ans
    i = 2
    while not isprime(n):
        if n % i == 0:
            ans.append(i)
            n = int(n / i)
        else:
            i += 1
    ans.append(n)
    ans = list(set(ans))
    return sorted(ans)