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
    n = int(input())
    '''
    Simple recursive code

    def count(curr):
        if curr > n:
            return 0
        if curr == n:
            return 1
        ans = 0
        for i in range(1,6):
            ans += count(curr+i)
            ans %= MOD
        return ans
    print(count(0))
    '''

    '''
    Recursive DP solution
    dp[i] : number of ways to get sum i

    dp = [-1]*n
    def count(curr):
        if curr > n:
            return 0
        if curr == n:
            return 1
        if dp[curr] != -1:
            return dp[curr]
        ans = 0
        for i in range(1,6):
            ans += count(curr+i)
            ans %= MOD
        dp[curr] = ans
        return ans
    print(count(0))
    '''

    '''
    Iterative DP solution
    dp[i] = number of ways to get sum i
    base case: dp[0] = 1
    transition : dp[i] = dp[i]+dp[i-j] where 1<=j<=6
    '''
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(1,min(6,i)+1):
            dp[i] += dp[i-j]
            dp[i] %= MOD
    print(dp[n])

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