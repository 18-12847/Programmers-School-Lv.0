def solution(spell, dic):
    spell.sort()
    spell = "".join(spell)
    ans = []
    for i in dic:
        tmp = list(i)
        ans.append("".join(sorted(tmp)))
    if spell in ans:
        return 1
    else:
        return 2