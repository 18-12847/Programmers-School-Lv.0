def solution(num, k):
    num = list(str(num))
    for i in num:
        if int(i) == k:
            return num.index(i)+1
    else:
        return -1