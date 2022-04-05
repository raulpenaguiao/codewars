def recoverSecret(triplets):
    edges = []
    pos = {}
    for triple in triplets :
        edges += [[triple[0], triple[1]]]
        edges += [[triple[0], triple[2]]]
        edges += [[triple[1], triple[2]]]
        pos[triple[0]] = 0
        pos[triple[1]] = 1
        pos[triple[2]] = 2
    n = len(pos.keys())
    str = []
    for i in range(n):
        str += ["."]
        for edge in edges:
            if pos[edge[1]]<= pos[edge[0]]:
                pos[edge[1]]= pos[edge[0]]+1
    for key in pos:
        str[pos[key]] = key
    return "".join(str)
