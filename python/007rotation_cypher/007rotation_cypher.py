
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def rot(char):
    for i in range(26):
        if char == upper[i]:
            return upper[(i+13)%26]
        if char == lower[i]:
            return lower[(i+13)%26]

def rot13(message):
    str = ""
    for char in message:
        if(char.isalpha()):
            str += rot(char)
        else:
            str += char
    return str
