def all(list):
    for b in list:
        if not(b):
            return False
    return True

def find_word(board, word):
    dir = [[1, 1], [0, 1], [-1, 1], [1, 0], [-1, 0], [1, -1], [0, -1], [-1, -1]]
    #print(board)
    #print("word = ", word)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                #print("We start a new round from i = ", i, " and j = ", j)
                vis = [[[i, j], [d for d in dir]]]
                while(len(vis) > 0 and len(vis) < len(word)):
                    #print("vis = ", vis)
                    if vis[-1][1] == []:#no possible directions, backtrack
                        vis = vis[:-1]
                        if vis != []:
                            vis[-1][1] = vis[-1][1][1:]
                    else:
                        d = vis[-1][1][0]
                        [x, y] = [vis[-1][0][0] + d[0], vis[-1][0][1] + d[1]]
                        bool = all([[x, y] != v[0] for v in vis]) #was this never visited?
                        if (0 <= x < len(board) and 0 <= y < len(board[0]) and bool and board[x][y] == word[len(vis)]):
                            vis.append([[x, y], dir])
                        else:
                            vis[-1][1] = vis[-1][1][1:]
                if len(vis) == len(word):
                    return True
    return False
