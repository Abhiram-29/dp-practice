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

MOD = 1_000_000_007

#region Solve

def solve():
    n,x = map(int,input().split())
    coins = list(map(int,input().split()))
    '''
    dp[i] = min number of coins required to make sum i
    dp[0] = 0
    dp[coin] = 1 for all coins given in the input
    transition: dp[i] = min(dp[i],dp[i-coin]+1)
    '''

    '''

    This solution gives TLE on CSES if python is used
    We might be evaluating a lot of unnecesasry states but 10^2*10^6 = 10^8 should pass

    dp = [float('inf')]*(x+1)
    dp[0] = 0
    for coin in coins:
        if coin <= x:
            dp[coin] = 1
    
    for i in range(1,x+1):
        for coin in coins:
            if i-coin >= 0:
                dp[i] = min(dp[i],dp[i-coin]+1)
    if dp[x] == float('inf'):
        print(-1)
    else:
        print(dp[x])
    '''


    '''
    Removed dp[coin] = 1 as it is covered in the main logic
    '''
    dp = [float('inf')]*(x+1)
    dp[0] = 0
    coins.sort()
    
    for i in range(1,x+1):
        for coin in coins:
            if i-coin < 0:
                break
            dp[i] = min(dp[i],dp[i-coin]+1)
    if dp[x] == float('inf'):
        print(-1)
    else:
        print(dp[x])



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