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
    s1,s2 = input(),input()
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    n,m = len(s1),len(s2)

    '''
    Recursive Solution (TLE)
    dp[i][j]: minimum number of operations required to match 
              the two string from positon i,j

    dp = [[-1]*m for _ in range(n)]

    def min_cnt(i,j):
        if j == m:
            return n-i
        if i >= n:
            return m-j
        if dp[i][j] != -1:
            return dp[i][j]
        add = min_cnt(i,j+1)+1
        remove = min_cnt(i+1,j)+1
        replace = min_cnt(i+1,j+1)+(0 if s1[i] == s2[j] else 1)
        dp[i][j] = min(add,remove,replace)
        return dp[i][j]
    print(min_cnt(0,0))
    '''


    '''
    Iterative solution(Accepted in c++ but TLE in python):
    dp[i][j]: minimum number of operations required to match the string
              till position i,j
    base case : dp[0][0] = 0
    final subproblem : dp[n][m]
    
    transition equation : dp[i][j] = min(min(dp[i][j-1],dp[i-1][j])+1,
                                         dp[i-1][j-1]+s[i]==s[j]

    '''

    dp = [[float('inf')]*(m+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j-1]+(0 if s1[i-1] == s2[j-1] else 1)
            if i > 0:
                dp[i][j] = min(dp[i][j],dp[i-1][j]+1)
            if j > 0:
                dp[i][j] = min(dp[i][j],dp[i][j-1]+1)
    print(dp[n][m])


# sys.setrecursionlimit(10**5)
solve()