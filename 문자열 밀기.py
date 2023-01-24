def solution(A, B):
    if A == B:
        return 0
    A, cnt = list(A), 0
    for _ in range(len(A)-1):
        A.insert(0, A.pop())
        cnt += 1
        if "".join(A) == B:
            return cnt
    else:
        return -1