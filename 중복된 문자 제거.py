def solution(my_string):
    ans = []
    my_string = list(my_string)
    for i in my_string:
        if not(i in ans):
            ans.append(i)
    return "".join(ans)