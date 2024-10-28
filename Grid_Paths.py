import os
import sys
from io import BytesIO, IOBase
import math

try:
    from icecream import ic
except:
    pass
#FOR USACO submission uncomment the below two lines #and change the file name
#sys.stdin = open("closing.in", "r")
#sys.stdout = open("closing.out", "w")

MOD = 1000000007

#region Solve

def solve():
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(input())
    
    '''
    dp[i][j]: number of paths form 0,0 to i,j
    base case: 0th row and column = 1 and if source or destination are trap return 0
    transition: dp[i][j] += up and left squares
    final subproblem : dp[n-1][n-1]
    '''
    if grid[0][0] == '*' or grid[n-1][n-1] == '*':
        print(0)
        return
    
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        if grid[i][0] == '.':
            dp[i][0] = 1
        else:
            break
    for i in range(n):
        if grid[0][i] == '.':
            dp[0][i] = 1
        else:
            break
    
    for i in range(1,n):
        for j in range(1,n):
            if grid[i][j] == '.':
                dp[i][j] += dp[i-1][j]+dp[i][j-1]
                dp[i][j] %= MOD
    for row in dp:
        print
    print(dp[n-1][n-1])
    


def main():
    solve()



# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()