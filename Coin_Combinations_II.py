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
    dp[i] = number of ordered ways to get sum i
    To count ordered ways The structure of the loops is important
    the outer loop should loop over the coins and the inner loop over i
    Code works in C++ but TLE in python
    '''
    coins.sort()
    dp = [0]*(x+1)
    dp[0] = 1

    for coin in coins:
        if coin > x:
            break
        for num in range(x+1):
            if dp[num] == 0:
                continue
            if num+coin > x:
                break
            dp[num+coin] += dp[num]
            dp[num+coin] %= MOD
    print(dp[x])

def main():
    solve()

input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()