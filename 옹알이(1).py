def solution(babbling):
    ans, tmp = ["aya", "ye", "woo", "ma"], []
    cnt = 0
    for i in range(len(ans)):
        tmp.append(ans[i])
    for i in range(len(ans)):
        for j in range(len(ans)):
            if i == j:
                continue
            tmp.append(ans[i] + ans[j])
    for i in range(len(ans)):
        for j in range(len(ans)):
            for k in range(len(ans)):
                if i == j == k or i == j or i == k or j == k:
                    continue
                tmp.append(ans[i] + ans[j] + ans[k])
    for i in range(len(ans)):
        for j in range(len(ans)):
            for k in range(len(ans)):
                for l in range(len(ans)):
                    if i == j == k == l or i == j == k or i == j == l or j == k == l or i == j or i == k or i == l or j == k or j == l or k == l:
                        continue
                    tmp.append(ans[i] + ans[j] + ans[k] + ans[l])
    for i in babbling:
        if i in tmp:
            cnt += 1
    return cnt