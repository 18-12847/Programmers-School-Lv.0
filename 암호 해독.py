def solution(cipher, code):
    answer = ''
    for i in range(code-1,len(cipher),code):
        answer += str(cipher[i])
    return answer