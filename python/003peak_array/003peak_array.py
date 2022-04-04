def pick_peaks(arr):
    ans = {"pos": [], "peaks": []}
    for i in range(len(arr)-2):
        if arr[i] < arr[i+1]:
            if arr[i+2] < arr[i+1]:
                ans["pos"]+=[i+1]
                ans["peaks"] += [arr[i+1]]
            elif arr[i+1] == arr[i+2]:
                j = i+3
                while(j < len(arr) and arr[j] == arr[i+1]):
                    j+=1
                if j < len(arr) and arr[i+1] > arr[j]:
                    ans["pos"]+=[i+1]
                    ans["peaks"] += [arr[i+1]]
    return ans
    #your code here
