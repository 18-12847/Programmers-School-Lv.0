def solution(array, n):
    array = sorted(array)
    ans = [abs(i-n) for i in array]
    return array[ans.index(min(ans))]