def solution(order):
    order = list(str(order))
    cnt = 0
    for i in range(len(order)):
        if not(order[i] == "0") and int(order[i]) % 3 == 0:
            cnt += 1
    return cnt