def solution(numbers):
    total = 0
    if 1 <= len(numbers) <= 100:
        for i in range(len(numbers)):
            if 0 <= numbers[i] <= 1000:
                total += numbers[i]
        return float(total/len(numbers))