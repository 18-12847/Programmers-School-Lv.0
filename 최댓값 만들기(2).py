def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if not(i == j):
                result.append(numbers[i] * numbers[j])
    return max(result)