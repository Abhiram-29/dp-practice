def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    dp = [[-1]*n for _ in range(n)]

    '''
    A is trying to maximize his score while B is trying to maximize his
    this is the same as B trying to minimizing A's score as S(A)+S(B) = sum(input)

    dp[i][j] = maximum possible difference if the game is played with
               with the subarray [i,j]
    A will try to maximize the difference while B will try to minimize it

    transition: dp[i][j] = max(x[i]-dp[i+1][j],x[j]-dp[i][j-1])
    base case: if i == j: dp[i][j] = arr[j] 
    final subproblem : dp[0][n-1]

    ans : total//2+dp[0][n-1]
    '''
    total = sum(arr)
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if i == j:
                dp[i][j] = arr[j]
                continue
            dp[i][j] = max(arr[i]-dp[i+1][j],arr[j]-dp[i][j-1])
    print((total + dp[0][n-1])//2)

solve()