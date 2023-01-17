def solution(i, j, k):
    ans = [list(str(i)) for i in range(i, j+1)]
    tot = 0
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if str(k) == str(ans[i][j]):
                tot += 1                
    return tot