def slide(word):
    if word == "!" or word == "?" or word == ".":
        return word
    return word[1:] + word[0] + "ay"


def pig_it(text):
    words = text.split(" ")
    nwords = [slide(str) for str in words]
    return " ".join(nwords)
