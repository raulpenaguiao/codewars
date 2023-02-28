def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk) == 10:
        x = 0
        y = 0
        for c in walk:
            if c == "n":
                y += 1
            if c == "s":
                y -= 1
            if c == "w":
                x -= 1
            if c == "e":
                x += 1
        return x == 0 and y == 0
    return False
    pass