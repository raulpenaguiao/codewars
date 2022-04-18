
def parseLetters(letter):
    if letter == "M":
        return 1000
    if letter == "D":
        return 500
    if letter == "C":
        return 100
    if letter == "L":
        return 50
    if letter == "X":
        return 10
    if letter == "V":
        return 5
    if letter == "I":
        return 1

def solution(roman):
    arr = [parseLetters(char) for char in roman]
    arr2 = []
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            arr2 += [arr[i-1]]
        else:
            arr[i] = arr[i] - arr[i-1]
    arr2 += [arr[-1]]
    tot = 0
    for k in arr2:
        tot+= k
    return tot
