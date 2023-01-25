def solution(chicken):
    tot = 0
    while chicken // 10 > 0:
        tot += chicken // 10
        chicken = (chicken % 10 + chicken // 10)
    return tot