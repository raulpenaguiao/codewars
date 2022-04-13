def sort_Second(list):
    return -list[1]

def allowed_Word(word):
    for char in word:
        if char != "'":
            return True
    return False


def top_3_words(text):
    str = ""
    forbiden_chars = [".", ",", "/", "#", "$", "%", "^", "&", "!", "?", "_", ":", ";", "-", "+", "="]
    for char in text:
        if not(char in forbiden_chars):
            str += char
        else:
            str+= " "
    str = str.lower()
    str = str.split(" ")
    str.sort()
    counter = [[str[0], 0]]
    for word in str:
        if counter[-1][0] == word:
            counter[-1][1] += 1
        else:
            counter += [[word, 1]]
    counter.sort(key=sort_Second)
    filtered_counter =[]
    for l in counter:
        if allowed_Word(l[0]):
            filtered_counter.append(l)
    size = min(len(filtered_counter), 3)
    return [filtered_counter[i][0] for i in range(size)]
