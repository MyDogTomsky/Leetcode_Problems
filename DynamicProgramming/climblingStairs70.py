# Leetcode70
# I can climb 1 or 2 steps each time, 
# When the N steps are given, Find the number of possible all cases.
# Approach : n steps = n - 1 steps + 1 step (each time)
#                               OR
#                      n - 2 stpes + 2 step (each time)


import time

def finding_ways(total_step):
    n = total_step
    total_case = [0]*n
    total_case[0] = 1
    total_case[1] = 2

    for step in range(2,n):
        total_case[step] = total_case[step-1] + total_case[step-2]

    return total_case[n-1]
    


def finding_second(stairs):
    m = stairs
    dp = [0] * (m+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for stair in range(3,m+1):
        dp[stair] = dp[stair - 1] + dp[stair - 2]

    return dp[m]    


start_time = time.time()

step2 = 2
step3 = 3
step44 = 44

outcome1 = finding_ways(step2)
print(f'\nThe first case has {step2} steps, and the possible ways climbing up are {outcome1}...\n')
outcome2 = finding_ways(step3)
print(f'\nThe second case has {step3} steps, and the possible ways climbing up are {outcome2}...\n')
outcome3 = finding_ways(step44)
print(f'\nThe third case has {step44} steps, and the possible ways climbing up are {outcome3}...\n')

print('\n============================= New way(Review):\n')
outcome11 = finding_second(step2)
print(f'\nThe first case has {step2} steps, and the possible ways climbing up are {outcome11}...\n')
outcome22 = finding_second(step3)
print(f'\nThe second case has {step3} steps, and the possible ways climbing up are {outcome22}...\n')
outcome33 = finding_second(step44)
print(f'\nThe third case has {step44} steps, and the possible ways climbing up are {outcome33}...\n')

end_time = time.time()
print(f'\n\n{end_time - start_time:.4f} SEC has consumed!')