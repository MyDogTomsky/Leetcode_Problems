# LeetCode 20
# Given a string -> s, which is having (,),{,},[,]
# s should be closed with orderly like ==> (,),{,},[,]

import time


def main(s:str) -> bool:

    print(f'\n\nThis case is {s} --> Testing Validation ...\n\n')

    ex = []
    orderis = {')':'(',']':'[','}':'{'}
    for one in s:
        if one in orderis.values():
            ex.append(one)
        elif one in orderis.keys():
            if ex and ex[-1] == orderis[one]:
                ex.pop()
            else:
                print('=> Invalid')            
                return False

    if not ex:
        print('-> Valid')
        return True
    else:
        print('=> Invalid')
        return False                



if __name__ == "__main__":

    start_time = time.time()

# making the test case

    list_s = ['()']
    list_s.append('()[]{}')
    list_s.append('(]')

# each case is tested by main function

    for s in list_s:
        main(s)

    end_time = time.time()
    print(f'\n\nTotal {end_time-start_time:.4f}-minute has consumed!')