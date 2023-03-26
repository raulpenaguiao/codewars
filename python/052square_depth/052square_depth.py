import queue

class Central_Pixels_Finder(Image):
    
    def central_pixels(self, colour):
        w = self.width
        h = self.height
        depth = [[h for _ in range(w)] for _ in range(h)]
        vis = [[0 for _ in range(w)] for _ in range(h)]
        q = queue.Queue()
        for i in range(w):
            q.push([0, i, 1])
            q.push([h-1, i, 1])
        for i in range(1, h-1):
            q.push([i ,0, 1])
            q.push([i, w-1, 1])
        for i in range(1, w-1):
            for j in range(1, h-1):
                if (self.data[i][j] != self.data[i][j-1]) or (self.data[i][j] != self.data[i][j+1]) or (self.data[i][j] != self.data[i+1][j]) or (self.data[i][j] != self.data[i-1][j]):
                    q.push([i, j, 1])
        while not q.empty():
            n = q.pop()
            if vis[n[0]][n[1]] == 0:
                vis[n[0]][n[1]] = 1
                depth[n[0]][n[1]] = min(depth[n[0]][n[1]], n[2])
                if n[0] > 0 and vis[n[0]-1][n[1]] == 0:
                    q.push([n[0]-1, n[1], n[2]+1])
                if n[0] < h-1 and vis[n[0]+1][n[1]] == 0:
                    q.push([n[0]+1, n[1], n[2]+1])
                if n[1] > 0 and vis[n[0]][n[1]-1] == 0:
                    q.push([n[0], n[1]-1, n[2]+1])
                if n[1] < w-1 and vis[n[0]][n[1]+1] == 0:
                    q.push([n[0], n[1]+1, n[2]+1])
        
  # your code goes here
