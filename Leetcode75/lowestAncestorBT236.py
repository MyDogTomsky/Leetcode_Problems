# Leetcode 236

# root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 ===> 3
# root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4 ===> 5
# root = [1,2], p = 1, q = 2  ===> 1
# Finding the highest the tree structure, including both p, q
# TreeNode => val (real value) / left and right => tree pointer to go

import time

class TreeNode:
    def __init__(self,val=0, left= None,right=None):
        self.val = val
        self.left = left
        self.right = right

# To get the value, not memory address 
    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


class lowestAncestorBT236:
    def finding_ancestor(self, root:TreeNode, p:TreeNode, q:TreeNode) ->TreeNode:

#recursion part(Divide)
        if not root: return None
        
        if root == p or root == q:
            return root
 
        left = self.finding_ancestor(root.left,p,q)
        right = self.finding_ancestor(root.right,p,q)

#recursion application part ->> to return!(Conquer)
        if left and right: 
            return root
        
        else:
            return left if left else right


if __name__=="__main__":
    
    go = time.time()
    exone = TreeNode(3)
    exone.left = TreeNode(5)
    exone.right = TreeNode(1)
    exone.left.left = TreeNode(6)
    exone.left.right = TreeNode(2)
    exone.left.right.left = TreeNode(7)
    exone.left.right.right = TreeNode(4)
    exone.right.left = TreeNode(0)
    exone.right.right = TreeNode(8)

    extwo = TreeNode(3)
    extwo.left = TreeNode(5)
    extwo.right = TreeNode(1)
    extwo.left.left = TreeNode(6)
    extwo.left.right = TreeNode(2)
    extwo.left.right.left = TreeNode(7)
    extwo.left.right.right = TreeNode(4)
    extwo.right.left = TreeNode(0)
    extwo.right.right = TreeNode(8)

    extrd = TreeNode(1,TreeNode(2))

    print(f'\n\nThere are THREE3 exanmples!!\n')
    print('First & Second => [3,5,1,6,2,0,8,null,null,7,4]')
    print('Third tree => [1,2]')
    p1,q1 = exone.left,exone.right
    p2,q2 = extwo.left,extwo.left.right.right
    p3,q3 = extrd,extrd.left

    iamancestor = lowestAncestorBT236()
    res1 = iamancestor.finding_ancestor(exone,p1,q1)
    res2 = iamancestor.finding_ancestor(extwo,p2,q2)
    res3 = iamancestor.finding_ancestor(extrd,p3,q3)

    print(f'\n\nFirst ===== finding ==== Satisfying with the condition(p:{p1}q:{q1}) ====> ANCESTOR : {res1.val}')
    print(f'Secnd ===== finding ==== Satisfying with the condition(p:{p2}q:{q2}) ====> ANCESTOR : {res2.val}')
    print(f'Third ===== finding ==== Satisfying with the condition(p:{p3}q:{q3}) ====> ANCESTOR : {res3.val}')


    exit = time.time()
    print(f'\n\nFinally, the process has finished. ---> It Took ___{exit-go:.4f} SECONDS! ')