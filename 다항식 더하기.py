def solution(poly):
    poly = poly.split(" + ")
    a, b = [], []
    for i in poly:
        if i.isdigit():
            b.append(int(i))
        elif len(i) == 1 and i[-1] == "x":
            a.append(1)
        else:
            a.append(int(i[:-1]))
    if sum(a) == 1:
        if sum(b) == 0:
            return "x"
        else:
            return f"x + {sum(b)}"
    elif sum(a) == 0:
        return f"{sum(b)}"
    elif sum(b) == 0:
        return f"{sum(a)}x"
    else:
        return f"{sum(a)}x + {sum(b)}"