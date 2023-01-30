def solution(dots):
    tmp = []
    for i in range(len(dots)):
        for j in range(i+1, len(dots)):
            x = (dots[i][0] - dots[j][0])
            y = (dots[i][1] - dots[j][1])
            if not(x == 0):
                tmp.append(y / x)
    for i in tmp:
        if tmp.count(i) > 1:
            return 1
    return 0