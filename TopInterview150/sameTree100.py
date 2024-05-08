# Leetcode 100 ==> O(n)
# p = [1,2,3] // q = [1,2,3] ===> true
# p = [1,2]   // q = [1,null,2] ===> false
# p = [1,2,1] // q = [1,1,2] ===> false

import time
from typing import Optional

class TreeNode:
    def __init__(self,val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Identical:
    def gocompare(self,tree_one:Optional[TreeNode],tree_two:Optional[TreeNode]) -> bool:
        if not tree_one and not tree_two:
            return True

        elif not tree_one or not tree_two or tree_one.val != tree_two.val:
            return False

        else:
            return self.gocompare(tree_one.left, tree_two.left) and self.gocompare(tree_one.right,tree_two.right)                 
       
# MainPoint --> keep Going Down?  --->  There was no point different values // faulty Nodes 
# last moment --> not a and not b ==> true // In other words, faluty nodes should be placed in the same space!

if __name__ == "__main__":

    launch = time.time()

# TEST1
    one1 = TreeNode(1)
    one1.left = TreeNode(2)
    one1.right = TreeNode(3)
    one2 = TreeNode(1)
    one2.left = TreeNode(2)
    one2.right = TreeNode(3) 
# TEST2
    two1 = TreeNode(1)
    two1.left = TreeNode(2)
    two2 = TreeNode(1)
    two1.right = TreeNode(2)
# TEST3
    third1 = TreeNode(1)
    third1.left = TreeNode(2)
    third1.right = TreeNode(1)
    third2 = TreeNode(1)
    third2.left = TreeNode(1)
    third2.right = TreeNode(2)

    tester = Identical()
    result1 = tester.gocompare(one1,one2)
    result2 = tester.gocompare(two1,two2)
    result3 = tester.gocompare(third1,third2)

    print(f'\n\n======================================\n\n')
    print(f'First cases: p = [1,2,3]   // q = [1,2,3] ===> {result1}')
    print(f'Second cases: p = [1,2]   // q = [1,null,2] ===> {result2}')
    print(f'Third cases: p = [1,2,1] // q = [1,1,2] ===> {result3} \n')

    finish = time.time()
    print(f'\n\n\tTime: {finish-launch:.5f} seconds.')
    