import time



def main(idx:int, one:str) -> str:

    print(f'\n{idx}: {one} --> ',end='')

    path = one.split('/')
    mpath = []

    for single in path:
        if single == '' or single == '.':
            continue
        elif single == '..':
            if mpath:
                mpath.pop()
        else:
            mpath.append(single)

    print('/'+'/'.join(mpath))                



if __name__ =='__main__':

    cases = ['/home/']

    cases.append('/home//foo/')
    cases.append('/home/user/Documents/../Pictures')
    cases.append('/../')
    cases.append('/.../a/../b/c/../d/./')

    for idx,one in enumerate(cases, start = 1):

        main(idx,one)
