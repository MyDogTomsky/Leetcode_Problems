# Leetcode509
# Simple Fibonacci Problem
# How to get the value of F(n) ??? 

import time

def fibonacci_value(sequence):
    n = sequence
    fibo = [0]*(n+1)
    fibo[0] = 0
    fibo[1] = 1

    for order in range(2,n+1):
        fibo[order] = fibo[order-1]+fibo[order-2]

    return fibo[n]

start_point = time.time()



for case in range(2,5):
    result = fibonacci_value(case)
    print(f'\nThe {case}th has fibonacci value : {result}\n')


end_point = time.time()
print(f'\nTotal {end_point - start_point:.4f}-second has consumed!')