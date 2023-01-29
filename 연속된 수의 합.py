def solution(num, total):
    tmp = []
    cnt = int(total / num) - int(num / 2)
    if num % 2 == 0:
        for i in range(cnt+1, cnt+num+1):
            tmp.append(i)
    else:
        for i in range(cnt, cnt+num):
            tmp.append(i)
    return tmp