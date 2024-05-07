# Leetcode 2390
# s:str ,which contains '*'
# When encountering '*' , we remove the left letter of it!
# "leet**cod*e" ---> 'lecoe'
# "erase*****" --> ''

import time

class removingStars2390:
    def new_string(self,s:str) -> str:

        ans = []
        print(f'\nGiven string is {s}... Processing -->', end = ' ')

        for e in s:
            if e == "*":
                if ans:
                    ans.pop()
            else:
                ans.append(e)

        print(''.join(ans))     
        

if __name__ == '__main__':
    
    start = time.time()
    experi = removingStars2390()
    experi.new_string('leet**cod*e')

    experi.new_string('erase*****')
    end = time.time()

    print(f'\n\n\tIt took {end-start:.6f} seconds!')