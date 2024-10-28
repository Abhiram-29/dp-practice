def solve():
    n,x = map(int,input().split())
    prices = list(map(int,input().split()))
    pages = list(map(int,input().split()))
    '''
    dp[i] = max number of pages that can be bought with i amount
    dp[0] = 0

    This gives TLE in python but works in CPP
    '''
    dp = [0]*(x+1)
    for j in range(n):
        for i in range(x,prices[j]-1,-1):
            dp[i] = max(dp[i],dp[i-prices[j]]+pages[j])
    print(dp[x])

solve()