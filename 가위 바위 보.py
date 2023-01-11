def solution(rsp):
    rsp = list(rsp)
    for i in range(len(rsp)):
        if rsp[i] == "2":
            rsp[i] = "0"
        elif rsp[i] == "0":
            rsp[i] = "5"
        elif rsp[i] == "5":
            rsp[i] = "2"
    return "".join(rsp)