# Leetcode 101

# root = [1,2,2,3,4,4,3] => True
# root = [1,2,2,null,3,null,3] => False


from typing import Optional

class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class TreeBasic:
    def treeisMirror(self,root:Optional[TreeNode]) -> bool:
        if not root:
            return True
        def innerMirror(left:TreeNode,right:TreeNode) -> bool:
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            else: 
                return innerMirror(left.left,right.right) and innerMirror(left.right, right.left)
        return innerMirror(root.left,root.right)    