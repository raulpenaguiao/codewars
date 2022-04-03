def move_zeros(array):
    new_arr = []
    count = 0
    for item in array:
        if item == 0 :
            count+=1
        else:
            new_arr += [item]
    for i in range(count):
            new_arr += [0]
    return new_arr
