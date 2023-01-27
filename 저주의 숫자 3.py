def solution(n):
    ans, tmp = [i for i in range(1, 201)], []
    for i in range(len(ans)):
        if ans[i] % 3 == 0:
            pass
        elif "3" in list(str(ans[i])):
            pass
        else:
            tmp.append(ans[i])
    return tmp[n-1]