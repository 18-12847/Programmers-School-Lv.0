def solution(numbers):
    tmp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(tmp)):
        if tmp[i] in numbers:
            numbers = numbers.replace(tmp[i],str(i))
    return int(numbers)