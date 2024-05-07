# Leetcode 71
# path e.g. =>  
#   /home/ -> /home , 
#   /home//foo/ -> /home/foo
#   /home/user/Documents/../Pictures -> /home/user/Pictures
#   /../ -> /
#   /.../a/../b/c/../d/./   ->  /.../b/d

import time


def main(idx:int, each:str) -> str:

    print()
    print(f'\n\n Case {[idx]}: {each} --- Modifying --->> ', end= '')
    
# .split('/') ==> spliting the strings based on '/' on a new list! <--> ''.join()
# /home///etc ---> ['','home','','','etc']

    path = each.split('/')
    new_path = ['']

    for unit in path:
        if unit == '' or unit == '.':
            continue
        elif unit == '..' and new_path:
            new_path.pop()
            if not new_path:
                new_path.append('/') 
            
        else:
            new_path.append(unit)

    print('/'.join(new_path))            


if __name__ =="__main__":

    go = time.time()
    print(f'\n\n\t<<< This program helps out to modify the PATH. >>>')
    cases = ['/home/']
    cases.append('/home//foo/')
    cases.append('/home/user/Documents/../Pictures')
    cases.append('/../')
    cases.append('/.../a/../b/c/../d/./')

    for idx,each in enumerate(cases,start=1):
        main(idx,each)

    end = time.time()
    
    print(f'\n\n\n\tTime: {end-go:.4f} seconds has consumed!\n')