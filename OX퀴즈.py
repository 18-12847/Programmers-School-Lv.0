def solution(quiz):
    ans, tmp = [], []
    for i in quiz:
        tmp.append(i.split(" = "))
        if eval(str(tmp[0][0])) == int(tmp[0][1]):
            ans.append("O")
        else:
            ans.append("X")
        tmp = []
    return ans