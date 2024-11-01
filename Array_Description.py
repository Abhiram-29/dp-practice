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
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    '''
    dp[i][j] = number of ways to create the array till index i if the current value is j
    if arr[i] == 0 then it can have the values v,v-1,v+1 where v = arr[i-1]
    transition : dp[i][j] = dp[i-1][j-1]+dp[i-1][j]+dp[i][j+1]
                 arr[i] != then only dp[i][arr[i]] is allowed and rest are 0
    base case: if arr[0] != 0 then:
                dp[0][arr[0]] = 1 (Only 1 way to create the array)
               else:
                dp[0][v] = 1 for all possible values v.
    final answer : sum(dp[n-1]) as the last element can be zero
    '''

    dp = [[0]*(m+1) for _ in range(n)]

    if arr[0] != 0:
        dp[0][arr[0]] = 1
    else:
        for i in range(1,m+1):
            dp[0][i] = 1

    for i in range(1,n):
        if arr[i] != 0:
            j = arr[i]
            for k in [j-1,j,j+1]:
                if k > 0 and k <= m:
                    dp[i][j] += dp[i-1][k]
                    dp[i][j] %= MOD
        else:
            for j in range(1,m+1):
                for k in [j-1,j,j+1]:
                    if k > 0 and k <= m:
                        dp[i][j] += dp[i-1][k]
                        dp[i][j] %= MOD
    ans = 0
    for num in dp[n-1]:
        ans += num
        ans %= MOD
    print(ans)

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