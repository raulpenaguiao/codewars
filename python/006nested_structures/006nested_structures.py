def same_structure_as(original,other):
    print(original, "v", other)
    bool1=isinstance(original,list)
    bool2=isinstance(other,list)
    if bool1 != bool2:
        return False
    if not(bool1) and not(bool2):
        return True
    if bool1 and bool2 and len(original) != len(other):
        return False
    for i in range(len(original)):
        if isinstance(original[i],list) and isinstance(other[i], list):
            if not(same_structure_as(original[i],other[i])):
                return False
        elif not( isinstance(original[i],list) ) and not( isinstance(other[i], list) ):
            pass
        else:
            return False
    return True
