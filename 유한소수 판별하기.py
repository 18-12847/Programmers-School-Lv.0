def solution(a, b):
    ans = [1, 2, 5]
    if b in ans:
        return 1
    a_tmp, b_tmp = [], [] 
    a_, b_ = a, b
    i = 2
    while a_ > 1:
        if a_ % i == 0:
            a_tmp.append(i)
            a_ = int(a_ / i)
        else:
            i += 1
    j = 2
    while b_ > 1:
        if b_ % j == 0:
            b_tmp.append(j)
            b_ = int(b_ / j)
        else:
            j += 1
    tot = 1
    for n in a_tmp:
        if n in b_tmp:
            tot *= n
            b_tmp.pop(b_tmp.index(n))
    a, b = int(a / tot), int(b / tot)
    b_tmp, b_ = [], b 
    j = 2
    while b_ > 1:
        if b_ % j == 0:
            b_tmp.append(j)
            b_ = int(b_ / j)
        else:
            j += 1
    b_tmp = list(set(b_tmp))
    if b in ans:
        return 1
    flag = 1
    for m in b_tmp:
        if m in ans:
            flag = 1
        else:
            return 2
    return flag