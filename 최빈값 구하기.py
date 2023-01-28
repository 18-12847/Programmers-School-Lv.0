def solution(array):
    array.sort()
    if len(array) == 1:
        return array[0]
    tmp = list(set(array))
    if len(tmp) == 1:
        return tmp[0]
    ans = [0] * len(tmp)
    for i in array:
        if i in tmp:
            ans[tmp.index(i)] += 1
    cnt = max(ans)
    for i in ans:
        if ans.count(cnt) > 1:
            return -1
    if len(tmp) == 1 and len(ans) == 1 and ans[0] > 1:
        return -1
    return tmp[ans.index(cnt)]