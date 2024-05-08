# Leetcode 104
# root = {3,9,20,null,null,15,7} -> 3
# root = {1,null,2} -> 2
# It needs the existence of the node every layer.

import time


class TreeValue:
    def __init__(self,val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Maxidentificator:
    def moving_height(self,midNode:TreeValue) -> int:
        if not midNode:
            return 0
        else: 
            return 1+ max(self.moving_height(midNode.left),self.moving_height(midNode.right))


if __name__ == "__main__":


    start = time.time()
    first_tree = TreeValue(3)
    first_tree.left = TreeValue(9)
    first_tree.right = TreeValue(20,TreeValue(15),TreeValue(7))
    sec_tree = TreeValue(1)
    sec_tree.right = TreeValue(2)

    trees = Maxidentificator()
    depth1 = trees.moving_height(first_tree)
    depth2 = trees.moving_height(sec_tree)
    print(f'\nHere are Two Trees.\n\n\tTree1: [3,9,20,null,null,15,7] / Tree2: [1,null,2]\n')
    print(f'\nThe First example tree has a {depth1}-layer.')
    print(f'\nThe Second example tree has a {depth2}-layer.')

    end = time.time()
    print(f'\n\n\tTime: {end-start:.4f} Sec.')