def solution(n, k):
    if 0 < n < 1000 and 0 <= k < 1000:
        z_fee = n // 10
        return (n * 12000) + (k * 2000) - (z_fee * 2000)