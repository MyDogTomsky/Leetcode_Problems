# Leetcode 872

# root1 = [3,5,1,6,2,9,8,null,null,7,4] 
# root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8] ==> True
# root1 = [1,2,3] // root2 = [1,3,2] ==> False

# It needs all last values list!(Comparing leaf nodes over two2 Trees)
import time
from typing import Optional

class TreeNode:
    def __init__(self,val=0,left = None, right= None):
        self.val = val
        self.left = left
        self.right = right


class investigator:
    def comparison(self,first_root: Optional[TreeNode], second_root:Optional[TreeNode]):
        
        def goingdfs(each_root):
            if not each_root:
                return []
            elif not each_root.left and not each_root.right:
                return [each_root.val]
            else:
                return goingdfs(each_root.left) + goingdfs(each_root.right)
        return goingdfs(first_root) == goingdfs(second_root)


if __name__ == "__main__":

    start = time.time()

    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)

    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(2)
    root2.right.right.left = TreeNode(9)
    root2.right.right.right = TreeNode(8)

    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)

    root4 = TreeNode(1)
    root4.left = TreeNode(3)
    root4.right = TreeNode(2)

    new_mc = investigator()
    result = new_mc.comparison(root1,root2)
    print(f'\n\nFirst Tree is --> [3,5,1,6,2,9,8,null,null,7,4]\nSecond Tree is --> [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]')
    print('WE are Identifying if they are same or not.... =====>  ',end= '')
    print(result)

    result2 = new_mc.comparison(root3,root4)
    print(f'\n\nThird Tree is --> [1,2,3]\nForuth Tree is --> [1,3,2]')
    print('WE are Identifying if they are same or not.... =====>  ',end= '')
    print(result2)

    end = time.time()
    print(f'\n\n\n\tTIME: {end-start:.4f} Sec')