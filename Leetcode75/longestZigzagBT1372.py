# Leetcode 1372

# root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1] -> 3
# root = [1,1,1,null,1,null,null,1,1,null,1] -> 4
# Finding the longest way by using the ZIGZAG WAY

import time
from typing import Optional

class TreeNode:
    def __init__(self,val = 0, left=None,right= None):
        self.val = val
        self.left = left
        self.right = right

class longestZigzagBT1372:
    def wayfinder(self,root:Optional[TreeNode],) -> int:
        self.longest = 0
        def waytoway(each_node,direction,length):

            if not each_node: 
                return 0
            self.longest = max(self.longest,length)

            if direction == "right":
                waytoway(each_node.right,"left",length+1)
                waytoway(each_node.left,"right",1)

            elif direction == "left":
                waytoway(each_node.left,"right",length+1)
                waytoway(each_node.right,"left",1) 
        
        
        waytoway(root, "right", 0)  
        waytoway(root, "left", 0) 
           

        return self.longest       


if __name__ =="__main__":

    depart = time.time()
    
    ex1 = TreeNode(1)
    ex1.right = TreeNode(1)
    ex1.right.left = TreeNode(1)
    ex1.right.right = TreeNode(1)
    ex1.right.right.left = TreeNode(1)
    ex1.right.right.right = TreeNode(1)
    ex1.right.right.left.right = TreeNode(1)
    ex1.right.right.left.right.right = TreeNode(1)



    ex2 = TreeNode(1)
    ex2.left = TreeNode(1)
    ex2.right = TreeNode(1)
    ex2.left.right = TreeNode(1)
    ex2.left.right.left = TreeNode(1)
    ex2.left.right.right = TreeNode(1)
    ex2.left.right.left.right = TreeNode(1)

    ex3 = TreeNode(1)    
    
        
    print(f'\n\nThere are THREE examples.===>\n')
    print(f'First: [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1] ')
    print(f'Second: [1,1,1,null,1,null,null,1,1,null,1]')
    print(f'Third: [1]\n\n')

    print(f'We are finding the longest way while seeking ONLY the ZIGZAG route!\n')
    print(f'=========================================================>>>>>>\n')
    
    
    solution = longestZigzagBT1372()
    res1 =solution.wayfinder(ex1)
    res2 = solution.wayfinder(ex2)
    res3 = solution.wayfinder(ex3)
    print(f'The longest path => ex1: {res1} /// ex2: {res2} // ex3: {res3}')

    arrive = time.time()
    print(f'\n\n\t Time: {arrive-depart:.3f} Seconds')
