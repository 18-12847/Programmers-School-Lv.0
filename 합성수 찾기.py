def solution(n):
    cnt = 0
    ans = [0] * (n+1)
    answer = 0
    for i in range(1, n+1):
        for j in range(1,i+1):
            if i % j == 0:
                ans[i] += 1
    for i in ans:
        if i > 2:
            cnt += 1
    return cnt