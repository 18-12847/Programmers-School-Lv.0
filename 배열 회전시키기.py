def solution(numbers, direction):
    if direction == "right":
        a = numbers.pop()
        numbers.insert(0,a)
        return numbers
    else:
        numbers.reverse()
        a = numbers.pop()
        numbers.reverse()
        numbers.append(a)
        return numbers