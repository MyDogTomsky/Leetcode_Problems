# Leetcode 5
# return the longest panlindromic substring in the given string!


import time

def processor(one_word):
    detc = []
    m = len(one_word)
    start = 0
    end = m-1
    mid = start + (end-start)//2

    while start >= end:
        for i in range(m):
            if one_word[start+i] != one_word[end-i]:



start_time = time.time()


ex_one = 'babad'
ex_two = 'cbbd'

string_list = [ex_one]
string_list.append(ex_two)

print(string_list)
for each_string in string_list:
    result = processor(each_string)
    print(f'The {each_string} has panlindromic patterns!\n\t\t\tThe longest one is {result}')


end_time = time.time()

print(f'\n\n\nTotal {end_time - start_time}-second has consumed.\n')