def to_camel_case(text):
    last_item = -1
    parts = []
    for index, item in enumerate(text):
        if item == "_" or item == "-":
            parts += [text[last_item+1:index]]
            last_item = index
    parts += [text[last_item+1:]]
    for i in range(1, len(parts)):
        parts[i] = parts[i].capitalize()
    return "".join(parts)
