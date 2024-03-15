# Leetcode 1
# The array with integers, using two numbers to make the required sum values.
# nums = [ , ] , target = (integer)
# Return the index of two numbers!!

import time

def two_sumup(nums,target):
    result = []
    comp_a = {ele:idx for idx,ele in enumerate(nums)}
    for idx, ele in enumerate(nums):
        rest =  target - ele 
        if rest in comp_a:
            if comp_a[rest] != idx:
                result = [idx, comp_a[rest]]
                break
    else: None
    return result


start_time = time.time()



case_one = [3,3]
target_one = 6
result = two_sumup(case_one,target_one)
print(f'\nThe targeted sum is {target_one},\nand we use the sequence ---> {result}\n')


case_two = [2,7,11,15]
target_two = 9
result2 = two_sumup(case_two,target_two)
print(f'\nThe targeted sum is {target_two},\nand we use the sequence ---> {result2}\n')


end_time = time.time()

print(f'\n\nReport:\n{end_time - start_time:.4f}-second has consumed!\n')