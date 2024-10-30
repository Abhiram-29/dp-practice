from bisect import bisect_left



def solve():
    n = int(input())

    arr = list(map(int,input().split()))
    '''
    dp[i] = minimum number that is at the end of a subseqence

            of length i


    final subproblem: len(dp)


    To update the dp we can use binary search to make the

    time complexity O(NlogN) instead of O(N^2)

    '''
    dp = []

    for num in arr:

        pos = bisect_left(dp,num)

        if pos == len(dp):
            dp.append(num)

        else:
            dp[pos] = num
    print(len(dp))

solve()