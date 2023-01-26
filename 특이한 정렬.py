def solution(numlist, n):
    ans, tmp = [], []
    numlist.sort(reverse=True)
    for i in numlist:
        tmp.append(abs(i-n))
    for _ in range(len(numlist)):
        ans.append(numlist.pop(tmp.index(min(tmp))))
        tmp.pop(tmp.index(min(tmp)))
    return ans