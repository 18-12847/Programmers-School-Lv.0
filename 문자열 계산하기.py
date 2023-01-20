def solution(my_string):
    li1 = my_string.split()
    d_stack = []
    op_stack = []
    for i in li1:
        if i.isdigit() and len(d_stack) > 0 and len(op_stack) > 0:
            if op_stack[-1] == "+":
                d_stack.append(d_stack.pop() + int(i))
            else:
                d_stack.append(d_stack.pop() - int(i))
        elif i.isdigit():
            d_stack.append(int(i))
        elif i == "+":
            op_stack.append("+")
        elif i == "-":
            op_stack.append("-")
    return d_stack.pop()