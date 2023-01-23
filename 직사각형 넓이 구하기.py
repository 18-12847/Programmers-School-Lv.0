def solution(dots):
    dots.sort()
    return abs(dots[0][0]-dots[2][0]) * abs(dots[0][1]-dots[1][1])