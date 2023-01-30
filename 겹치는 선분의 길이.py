def solution(lines):
    cnt = 0
    if lines[0][1] == lines[1][0] and lines[1][1] == lines[2][0]:
        return 0
    tmp, ans = [], []
    a = [i for i in range(lines[0][0], lines[0][1]+1)]
    b = [i for i in range(lines[1][0], lines[1][1]+1)]
    c = [i for i in range(lines[2][0], lines[2][1]+1)]
    for i in range(len(a)-1):
        tmp.append((a[i] + a[i+1]) / 2)
    for i in range(len(b)-1):
        tmp.append((b[i] + b[i+1]) / 2)
    for i in range(len(c)-1):
        tmp.append((c[i] + c[i+1]) / 2)
    for i in range(len(tmp)):
        if tmp[i] in ans:
            continue
        elif tmp.count(tmp[i]) > 1:
            ans.append(tmp[i])
    return len(ans)