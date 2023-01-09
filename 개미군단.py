def solution(hp):
    answer = 0
    answer += hp//5
    hp -= (hp//5 * 5)
    if hp >= 3:
        answer += 1
        hp -= 3 
        answer += hp // 1
    else:
        answer += hp // 1
    return answer