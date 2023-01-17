def solution(before, after):
    before = sorted(list(before))
    after = sorted(list(after))
    if "".join(before) == "".join(after):
        return 1
    return 0