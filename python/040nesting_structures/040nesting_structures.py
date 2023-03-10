def same_structure_as(original, other):
    a = isinstance(original, list)
    b = isinstance(other, list)
    if a == True and b == True:
        if len(original) == len(other):
            return all([same_structure_as(k1, k2) for k1, k2 in zip(original, other)])
        return False
    return a == b
