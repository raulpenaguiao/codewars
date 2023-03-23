def rot_90_clock(strng):
    t = strng.split("\n")
    n = len(t)
    return "\n".join(["".join([ t[n-i-1][j]for i in range(n)]) for j in range(n)])
    # your code       
def diag_1_sym(strng):
    t = strng.split("\n")
    n = len(t)
    return "\n".join(["".join([ t[i][j]for i in range(n)]) for j in range(n)])
    # your code
def selfie_and_diag1(strng):
    t = strng.split("\n")
    n = len(t)
    return "\n".join(["".join([ t[j][i]for i in range(n)] + ["|"] + [ t[i][j] for i in range(n)]) for j in range(n)])
    # your code
def oper(fct, s):
    print("fct = ", fct)
    return fct(s)
    # your code
