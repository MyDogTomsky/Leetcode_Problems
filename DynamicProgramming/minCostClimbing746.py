# Leetcode 746
# Find the efficient way with minimum cost to the top!

import time

def minSum_toFinal(given_stair):
    n = len(given_stair)
    dp = [0]*(n+1)
    
    for order in range(2,n+1):
        dp[order] = min(dp[order-1]+given_stair[order-1], dp[order-2]+given_stair[order-2])


    return dp[n]


def min_totalCost(stair_info):

    m = len(stair_info)
    dp = [0] * (m+1)

    for stair in range(2,m+1):
        dp[stair] = min(dp[stair-1]+stair_info[stair-1],dp[stair-2]+stair_info[stair-2])

    return dp[m]    

departure = time.time()

all_cases = []

case1 = [10,15,20]
case2 = [1,100,1,1,1,100,1,1,100,1]

all_cases.append(case1)
all_cases.append(case2)

for case in all_cases:
    result = minSum_toFinal(case)
    print(f'\nThis case ==> {case} costs {result}!!!\n')

print('\n====================== New:(review)\n\n')
for case in all_cases:
    result2 = min_totalCost(case)
    print(f'\nThis case ==> {case} costs {result2}!!!\n')

arrival = time.time()

print(f'\n{arrival - departure:.4f} seconds has taken!')