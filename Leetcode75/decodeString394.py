# Leetcode 394
# s = "3[a]2[bc]" --> "aaabcbc"
# s = "3[a2[c]]" --> "accaccacc"
# s = "2[abc]3[cd]ef" --> "abcabccdcdcdef"

import time

class decodeString394:
    def go_decode(self,s:str) -> str:
        info_stack = []
        num = 0
        temp = ''
        print(f'\nGiven code :{s} --- Decoding ---- >>> ',end = '')

        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
                # if the integer is two-digit numbers, we should consider it.
            elif i == '[':
                info_stack.append((temp,num))
                temp= ''
                num = 0

            elif i == ']':
                last,inner_num = info_stack.pop()
                temp = last + int(inner_num)*temp

            else:
                temp += i      
        print(temp)
        return temp               


if __name__ == "__main__":

    go = time.time()
    decoder = decodeString394()
    decoder.go_decode("3[a]2[bc]")
    decoder.go_decode("3[a2[c]]")
    decoder.go_decode('2[abc]3[cd]ef')
    decoder.go_decode('100[leetcode]')
    finish = time.time()

    print(f'\n\n\t{finish-go:.5f} SECONDS TOOK!')