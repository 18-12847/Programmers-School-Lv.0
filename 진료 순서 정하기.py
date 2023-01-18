def solution(emergency):
    cnt = [1] * len(emergency)
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if not (i == j) and emergency[i] > emergency[j]:
                cnt[j] += 1
    return cnt