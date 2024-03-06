# Leetcode 1137


def finding_tribonacci(order):
    m = order
    tribo = [0]*(m+3)
    tribo[0] = 0
    tribo[1] = 1
    tribo[2] = 1
    for order in range(3,m+1):
        tribo[order] = tribo[order-1] + tribo[order-2] + tribo[order - 3]
    return tribo[m]    

import time

start_pt =time.time()

case4 = 4
case25 = 25
result4= finding_tribonacci(case4)
result25 = finding_tribonacci(case25)
print(f'\n{case4}th digit in the Tribonacci array is {result4}\n')
print(f'\n{case25}th digit in the Tribonacci array is {result25}\n')

end_pt = time.time()

print(f'\n{end_pt - start_pt:.4f} seconds took!')