def solution(my_string):
    ans = []
    for i in my_string:
        if i.isalpha():
            ans.append(" ")
        elif i.isdigit():
            ans.append(i)
    tmp = "".join(ans)
    ans = map(int, tmp.split())
    return sum(ans)