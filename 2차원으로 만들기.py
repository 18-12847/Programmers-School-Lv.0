def solution(num_list, n):
    answer = []
    ans = []
    cnt = 0
    for i in range(int(len(num_list)/n)):
        for j in range(n):
            ans.append(num_list[cnt])
            cnt += 1
        answer.append(ans)
        ans = []
    return answer