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
    num = int(input())

    '''
    dp[i] = min number of operations to make i 0
    dp[i] = min(dp[i],dp[i-digit])
    '''

    '''
    Recursive DP solution

    dp = [-1]*(num+1)
    dp[0] = 0
    def count(n):
        if dp[n] != -1:
            return dp[n]
        t = n
        ans = float('inf')
        while n:
            digit = n%10
            n //= 10
            if t-digit >= 0 and digit != 0:
                ans = min(ans,count(t-digit))
        dp[n] = ans+1
        return ans+1

    print(count(num))
    '''

    dp = [float('inf')]*(num+1)
    dp[0] = 0

    for i in range(1,num+1):
        temp = i
        while temp:
            digit = temp%10
            temp //= 10
            dp[i] = min(dp[i],dp[i-digit]+1)
    print(dp[num])

def main():
    sys.setrecursionlimit(2*10**5)
    solve()


if __name__ == "__main__":
    main()