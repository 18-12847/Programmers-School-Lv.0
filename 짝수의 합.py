def solution(n):
    sum = 0
    if 0 < n <= 1000:
        for i in range(0, n+1):
            if i % 2 == 0:
                sum += i
        return sum