
#generate neighbours information
neig = [[[] for i in range(9)] for j in range(9)]
for i in range(9):
    for j in range(9):
        for k in range(9):
            if not i == j:
                neig[i][k].append([j, k])
                neig[k][i].append([k, j])
for t in range(3):
    for s in range(3):
        for u in range(3):
            for v in range(3):
                for y in range(3):
                    for w in range(3):
                        if not(u == v and y == w):
                            neig[3*t+u][3*s+y].append([3*t+v,3*s+w])
                            #connect 3*t + u , 3*s + y with 3*t + v, 3*s + w
#print(neig[3][8])


                            
class Board:
    def __init__(self, board):
        self.board = board[:]#does it save the reference or the list? I want the list
        self.poss = [[[1 for _ in range(9)] for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if not board[i][j] == 0:
                    self.infer([i, j, board[i][j]])
    
    def infer(self, info):
        for xi, xj in neig[info[0]][info[1]]:
            self.poss[xi][xj][info[2]-1] = 0
        for k in range(9):
            if not k == info[2]-1:
                self.poss[info[0]][info[1]][k] = 0
    
    def is_valid(self):
        for i in range(9):
            for j in range(9):
                if sum(self.poss[i][j]) == 0:
                    return False
        return True                    
                    
    def instance(self):
        # = [[i, j], k] where it suggests placing the value k in entry i, j.
        #it returns [[0, 0], 0] if sudoku is complete
        for i in range(9):
            for j in range(9):
                if not sum(self.poss[i][j]) == 1:
                    for k in range(9):
                        if self.poss[i][j][k] == 1:
                            return [[i, j], k]
        return [[0, 0], 0]
    
    
    def instanciate(self, inst):
        new_board = self.board[:]
        new_board[inst[0][0]][inst[0][1]] = inst[1]+1
        return Board(new_board)
        
        
    def remove(self, inst):
        self.poss[inst[0][0]][inst[0][1]][inst[1]] = 0
        if sum(self.poss[inst[0][0]][inst[0][1]]) == 1:
            self.infer(inst[0][0], inst[0][1], inst[1])
    
    
    def print(self):
        for i in range(9):
            print( "|".join(["".join([str(k) for k in self.poss[i][j]]) for j in range(9)]))
        for l in self.board:
            print(" ".join([str(k) for k in l]))
    
def solve(board):
    path = []
    board_obj = Board(board)
    while len(path) < 100:
        print("len = ", len(path))
        board_obj.print()
        if board_obj.is_valid() == False:
            #BACKTRACK
            print("BACKTRACKING")
            if path == []:
                return "NO SOLUTION EXISTS"
            board_obj.print()
            board_obj = path[-1][0]
            board_obj.remove(path[-1][1])
            board_obj.print()
            path = path[:-1]
        else:
            #find instance to instantiate
            inst = board_obj.instance() 
            # = [[i, j], k] where it suggests placing the value k in entry i, j.
            #it returns [[0, 0], 0] if sudoku is complete
            if inst[1] == 0:
                return board_obj.board
            else:
                #GO FORWARD
                print("Instanciating ", inst)
                path.append([Board(board_obj.board), inst])
                board_obj = board_obj.instanciate(inst)
    pass
