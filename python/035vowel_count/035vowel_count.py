def get_count(sentence):
    l = ["a", "e", "i", "o", "u"]
    return sum([sentence.count(c) for c in l])
