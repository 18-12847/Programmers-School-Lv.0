def solution(age):
    age = list(str(age))
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    result = []
    for i in age:
        result.append(alpha[int(i)])
    return "".join(result)