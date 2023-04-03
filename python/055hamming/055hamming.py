ham = []

lim2 = 150
lim3 = 90
lim5 = 20

pow2 = [2**j for j in range(lim2)]
pow3 = [3**j for j in range(lim3)]
pow5 = [5**j for j in range(lim5)]

for i in range(lim2):
    for j in range(lim3):
        for k in range(lim5):
            s = pow2[i]*pow3[j]*pow5[k]
            ham += [s]
ham.sort()

def hamming(n):
    return ham[n-1]
