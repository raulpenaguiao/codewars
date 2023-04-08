def arr_adder(arr):
    arr1 = [[arr[i][j] for i in range(len(arr))] for j in range(len(arr[0]))]
    text = []
    for line in arr1:
        text += ["".join(line)]
    return " ".join(text)
