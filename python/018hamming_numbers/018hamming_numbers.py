"""def is_ham(n):
    if(n%7 == 0 or n%11 == 0 or n%13 == 0 or n%17 == 0 or n%19 == 0 or n%23 == 0 or n%29 == 0 or n%31 == 0 or n%37 == 0 or n%41 == 0 or n%43 == 0):
        return False
    k = n
    while(k%2 == 0):
        k//= 2
    while(k%3 == 0):
        k//= 3
    while(k%5 == 0):
        k//= 5
    return k == 1

counter = 0
ham = []
n=1
while(counter < 600):
    if(is_ham(n)):
        ham.append(n)
        counter += 1
    n+= 1
print(n)
def hamming(n):
    return ham[n-1]"""

def secondEle(list):
    return -list[1]

ham = [1]
el2 = [[1, 0, 0], 2]
el3 = [[0, 1, 0], 3]
el5 = [[0, 0, 1], 5]
counter = 1
queue = [el5, el3, el2]
LIM = 5000
while(counter <= LIM):
    el = queue.pop()
    if(ham[counter-1] < el[1]):
        ham.append(el[1])
        counter += 1
        el2 = [[el[0][0] + 1, el[0][1], el[0][2]], el[1]*2]
        queue.append(el2)
        el3 = [[el[0][0], el[0][1] + 1, el[0][2]], el[1]*3]
        queue.append(el3)
        el5 = [[el[0][0], el[0][1], el[0][2] + 1], el[1]*5]
        queue.append(el5)
        queue.sort(key = secondEle)
def hamming(n):
    return ham[n-1]
