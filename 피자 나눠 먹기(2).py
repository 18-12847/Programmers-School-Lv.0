def solution(n):
    x = 6
    if n < 4:
        return 1
    else:
        for i in range(max(n, x),n*x+1):
            if i % n == 0 and i % x == 0:
                return i // 6