def linked_list_from_string(s):
    return parse_list(s.split(" -> "))

def parse_list(l):
    if len(l) == 0 or l[0] == "None":
        return None
    if len(l) == 1 or l[1] == "None":
        return Node(int(l[0]))
    return Node(int(l[0]), parse_list(l[1:]))
