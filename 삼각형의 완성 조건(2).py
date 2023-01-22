def solution(sides):
    sides.sort(reverse = True)
    return sides[0] - (sides[0] - sides[1]) + sides[1] - 1