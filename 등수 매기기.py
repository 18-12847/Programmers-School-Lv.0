def solution(score):
    ans = [0] * len(score)
    cnt, tmp = 1, 0
    for i in range(len(score)):
        score[i] = sum(score[i]) / 2
    for i in range(len(score)):
        for j in range(score.count(max(score))):
            if ans.count(0) == 0:
                break
            ans[score.index(max(score))] = cnt
            score[score.index(max(score))] = -len(score)
            tmp += 1
        cnt += tmp
        tmp = 0
    return ans