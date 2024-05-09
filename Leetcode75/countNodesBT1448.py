# Leetcode 1448
# root = [3,1,4,3,null,1,5] -> 4
# root = [3,3,null,4,2] -> 3
# root = [1] -> 1
import time

class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class countNodesBT1448:
    def thisisgood(self,firstroot:TreeNode) -> int:
        def eachway(root,max_val):
            
            if not root:
                return 0
            if root.val >= max_val:
                good = 1
                max_val = root.val
            else: 
                good = 0
    # The reason NOT => return 0 : There is possibility the existence of good child nodes!!            
    # e.g. the order : {3,4,2}  --> {3,4,2,5}
            good += eachway(root.left, max_val)
            good += eachway(root.right, max_val)

            return good 
        return eachway(firstroot,firstroot.val)  


if __name__ == '__main__':
    

    start = time.time()
    print(f'\n\nHow many good nodes? Here are two examples!\n')
    oneex = TreeNode(3)
    oneex.left = TreeNode(1,TreeNode(3),None)
    oneex.right = TreeNode(4,TreeNode(1),TreeNode(5))

    twoex = TreeNode(3)
    twoex.left = TreeNode(3,TreeNode(4),TreeNode(2))

    counter = countNodesBT1448()
    result1 = counter.thisisgood(oneex)
    result2 = counter.thisisgood(twoex)

    print(f'\n\nFirst tree has {result1} Good Nodes!')
    print(f'Second tree has {result2} Good Nodes!')
    
    end = time.time()
    print(f'\n\n\tThis Process Took {end-start:.5f} Seconds.')