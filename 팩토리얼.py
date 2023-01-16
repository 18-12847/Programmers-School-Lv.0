def solution(n):
    if n == 3628800:
        return 10
    tot = 1
    cnt = 0
    for i in range(1,11):
        tot *= i
        if tot > n:
            return cnt
        cnt += 1