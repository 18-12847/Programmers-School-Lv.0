def solution(bin1, bin2):
    bin1 = list(bin1)
    bin1.reverse()
    a = 0
    for i in range(len(bin1)):
        a += (int(bin1[i]) * (2 ** i)) 
    
    bin2 = list(bin2)
    bin2.reverse()
    b = 0
    for i in range(len(bin2)):
        b += (int(bin2[i]) * (2 ** i)) 
    c = a + b
    c = list(str(bin(c)))
    c = c[2:]
    return "".join(c)