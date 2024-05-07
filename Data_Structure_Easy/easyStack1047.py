# Leetcode 1047 / Level: Easy / Topic: Stack
# Given string -> one
# abbaca -> ca / azxxzy -> ay

import time

def main(idx:int,one:str) -> str:

    print(f'\nString {[idx]} : {one} .... Processing ==> ',end= ' ')

    comp = [one[0]]

    for single in one[1:]:
        if comp and comp[-1] == single:
            comp.pop()
        else:
            comp.append(single)

    return print(''.join(comp))            



if __name__ == "__main__":


    start = time.time()
    cases = ['abbaca']
    cases.append('azxxzy')

    for idx,one in enumerate(cases,start=1):
        main(idx,one)

    ended = time.time()

    print(f'\n\nTime: {ended-start:.4f} seconds consumed\n')