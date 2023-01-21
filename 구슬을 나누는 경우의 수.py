def fact(a):
    if a == 1:
        return 1
    return a * fact(a-1)

def solution(balls, share):
    if balls == share:
        return 1
    else:
        return fact(balls) / (fact(balls-share) * fact(share))