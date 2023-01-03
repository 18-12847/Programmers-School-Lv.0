def solution(numbers):
    answer = sorted(numbers)
    return answer[-1] * answer[-2]