# Leetcode 740
# if I pick the num in the given array,
# when the num is m, I can earn the m points,
# and every m-1, m+1 elements are deleted.
# Please return the maximum points I can get in the given array!


import time

def calculating(each_set):
    m = max(each_set)
    new_set = [0]*(m+2)
    for num in each_set:
        new_set[num] += num

    dp = [0]*(m+2)
    dp[1] = new_set[1]
    dp[2] = max(new_set[1],new_set[2])
    for i in range(3,m+1):
        dp[i] = max(dp[i-2]+new_set[i],dp[i-3]+new_set[i-1])    

    # why do the range of new_set, dp m+2? ===> WHEN nums = [1], indexErr prevention.
    return dp[m]

starting = time.time()

card = [[3,4,2]]
card2 = [2,2,3,3,3,4]
card.append(card2)

for a_set in card:
    pts = calculating(a_set)
    print(f'\nTHIS {a_set} can have maximum {pts} points!\n')


ending = time.time()


print(f'\n\n{ending - starting:.4f} seconds consumed.\n')