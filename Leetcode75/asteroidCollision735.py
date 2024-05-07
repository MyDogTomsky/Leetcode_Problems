# Leetcode 735
# asteroids = [5,10,-5] ==> [5,10]
# asteroids = [8,-8]    ==> []
# asteroids = [10,2,-5] ==> [10]

import time
from typing import List

class asteroidCollision735:
    def survivor(self,asteroids: List[int]) -> List[int]:
        ans = []
        print(f'\nCurrently, we have these Asteroids ==> {asteroids}')
        print(f'Some asteroids are destoryed ---> Remained: ',end='')
        for unit in asteroids:
            while ans and unit < 0 < ans[-1]:
                if ans[-1] < abs(unit):
                    ans.pop()
                elif ans[-1] == abs(unit):
                    ans.pop()
                    break      
                else: 
                    break         
            
            else:
                ans.append(unit)
            # while-else, else: ==> when not break!     

        return print(ans)
                
# This one should be 

if __name__ =='__main__':
    
    start = time.time()
    epl = asteroidCollision735()
    
    epl.survivor([5,10,-5])
    epl.survivor([8,-8])
    epl.survivor([10,2,-5])
    end = time.time()

    print(f'\n\n\t Time: {end-start:.5f} Seconds!')

    