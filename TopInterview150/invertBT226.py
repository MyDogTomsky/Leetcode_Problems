# Leetcode 226
# root = [4,2,7,1,3,6,9] => [4,7,2,9,6,3,1]
# root = [2,1,3] => [2,3,1]
# root = [] => []

import time
from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Inverter:
    def goingChange(self,root:Optional[TreeNode]) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.goingChange(root.right), self.goingChange(root.left) 

        return root
# every root -> changing below left and right nodes! 

if __name__ == "__main__":

    launch = time.time()

# one1
    one1 = TreeNode(4)
    one1.left = TreeNode(2,TreeNode(1),TreeNode(3))
    one1.right = TreeNode(7,TreeNode(6),TreeNode(9))


# TEST2
    two1 = TreeNode(2,TreeNode(1),TreeNode(3))

    tester = Inverter()
    result1 = tester.goingChange(one1)
    result2 = tester.goingChange(two1)

    print(f'\n\n======================================\n\n')
    print(f'First cases: [4,2,7,1,3,6,9],\nexpected result = [4,7,2,9,6,3,1] \n===> {result1}')
    print(f'Second cases:  [2,1,3],\nexpected result = [2,3,1] ===> {result2}')


# It should be listed the changed tree by using deque. 
# But I didn't implement to change the structure from Tree to List.

    finish = time.time()
    print(f'\n\n\tTime: {finish-launch:.5f} seconds.')                   