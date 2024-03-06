# Leetcode 198
# Robbery couldn't make it for adjacent houses!
# maximum amount of money I can rob!

import time

def efficient_robbery(house_map):
    n = len(house_map)
    dp = [0]*(n+1)
    # if the house I rob is only one, 
    # when the length of dp is n, the program can't assign the dp[2]!(Runtime Err)

    dp[1] = house_map[0]
    dp[2] = max(house_map[0],house_map[1])

    for h in range(3,n+1):
        dp[h] = max(dp[h-2]+house_map[h-1],dp[h-3]+house_map[h-2])
    
    return dp[n]

start_clock = time.time()
end_clock = time.time()

map1 = [1,2,3,1]
map2 = [2,7,9,3,1]
housing_map = []
housing_map.append(map1)
housing_map.append(map2)

for map in housing_map:
    result = efficient_robbery(map)
    print(f'\nAfter researching all the houses,\nCurrent the value of each house is {map}')
    print(f'\t\t\tSo, we are gonna robber the selected way, total amount will be {result}\n')    

print(f'\n\n{end_clock - start_clock:.4f} seconds has consumed!')