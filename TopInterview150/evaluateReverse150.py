# Leetcode 150
# tokens = ["2","1","+","3","*"] -> (2+1)*3 = 9
# tokens = ["4","13","5","/","+"] -> (4+ (13/5)) = 6
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] -> 22


import time
from typing import List

class evaluateReverse150:
    def evalRPN(self, tokens: List[str]) -> int:
        
        print(f'\n\nGiven tokens ---> {tokens} .... Calculating... ==> ',end = '')

        digit_stack = []

        for unit in tokens:
            if unit in {"+","-","*","/"}:
                latter = digit_stack.pop()
                former = digit_stack.pop()

                if unit == '+':
                    digit_stack.append(former+latter)
                elif unit == '-':
                    digit_stack.append(former-latter)
                elif unit == '*':
                    digit_stack.append(former*latter)
                else:
                    digit_stack.append(int(former/latter))                 

            else:
                digit_stack.append(int(unit))

        print(f'===> {digit_stack[0]}')
        


if __name__ =="__main__":

    start = time.time()

    po_cal = evaluateReverse150()
    po_cal.evalRPN(["2","1","+","3","*"])
    po_cal.evalRPN(["4","13","5","/","+"])
    po_cal.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])

    end = time.time()

    print(f'\n\n\t !!! {end-start:.5f} seconds !!!')