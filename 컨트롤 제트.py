def solution(s):
    ans = []
    s = list(s.split())
    for i in range(len(s)):
        if s[i] == "Z":
            ans.pop()
        else:
            ans.append(s[i])
    return sum(list(map(int, ans)))