def solution(array):
    array = list(str(array))
    tot = 0
    for i in array:
        if i == str(7):
            tot += 1 
    return tot