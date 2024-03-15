# Leetcode 49
# Given group of strings array: strs[]
# return the strings which can be anagramed to each other.

import time


def dec_anagram(strings):
    detector = dict()
    for word in strings:
        ordered_word = ''.join(sorted(word))
        if ordered_word in detector:
            detector[ordered_word].add(word)
        else: 
            detector[ordered_word] = {word} 

    return [list(one) for one in detector.values()]          




def detector_ana(group):

    group_dict = dict()
    n = len(group)
    for idx,word in enumerate(group):
        one_set = set()
        for char in word:
            one_set.add(char)
        group_dict[idx]= one_set

    total_det = {}
    for i in range(n):
        single_det = {}
        for j in range(n):
            if group_dict[i] == group_dict[j]:
                single_det.add(i)
                single_det.add(j)
           
        total_det.add(frozenset(single_det))

    result = []
    for each_result in total_det:
        result.append(list(group[idx] for idx in each_result))

    return result    



start_time = time.time()

group_first = ["eat","tea","tan","ate","nat","bat"]
group_sec = [""]
group_third = ["a"]

group_list = [group_first]
group_list.append(group_sec)
group_list.append(group_third)

for each_string in group_list:
    outcome = dec_anagram(each_string)
    print(f'\n\nThere is a {each_string} list,\nTo determine if there are ANAGRAMS!\n')
    print(f'ANAGRAM ------ >>> {outcome}\n')


print(f'\n\n\nFirst Approach: ================= Using frozenset() =============== \n\n')
for each_group in group_list:
    result = detector_ana(each_group)
    print(f'\n\nThere is a {each_group} list,\nTo determine if there are ANAGRAMS!\n')
    print(f'ANAGRAM ------ >>> {result}\n\n')

end_time = time.time()

print(f'\n\nTotal {end_time-start_time:.4f}-second has consumed!')