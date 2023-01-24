def solution(id_pw, db):
    id_, pw = id_pw[0], id_pw[1]
    ans = ""
    for i in range(len(db)):
        if id_ in db[i] and pw in db[i]:
            ans = "login"
            break
        elif id_ in db[i] and not(pw in db[i]):
            ans = "wrong pw"
            break
        else:
            ans = "fail"
    return ans