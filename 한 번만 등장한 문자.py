def solution(s):
    tmp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    cnt = dict()
    s = list(s)
    s.sort()
    ans = ""
    for i in s:
        if i in tmp:
            cnt[i] = cnt.get(i,0)+1
    for k, v in cnt.items():
        if v == 1:
            ans += k
    return ans