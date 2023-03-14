def validate_pin(pin):
    l = len(pin)
    if l == 4 or l == 6:
        for c in pin:
            if not c.isnumeric():
                return False
        return True
    return False
    #return true or false
