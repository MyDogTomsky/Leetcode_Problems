# Leetcode 437

# root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8   ==> 3
# root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 ==> 3
# starting point doesn't need to be from the first root!

import time

class TreeNode:
    def __init__(self,val = 0, left= None,right = None):
        self.val = val
        self.left = left
        self.right = right

class pathSumthree437:
    def findingSum(self,root:TreeNode,target_num) -> int:
       
        if not root:
            return 0
        def targetsum(each_root,num):

            if not each_root:
                return 0
            
            num += each_root.val
            if num != target_num:
                cnt = 0
            else:
                cnt = 1
                
            cnt += targetsum(each_root.left,num)
            cnt += targetsum(each_root.right,num)

            return cnt
        '''
        allc = 0
        allc += self.findingSum(root.left,target_num) 
        allc += self.findingSum(root.right,target_num)
'''
        return targetsum(root,0) + self.findingSum(root.left,target_num) + self.findingSum(root.right, target_num)

if __name__ == "__main__":

    founder = pathSumthree437()
    going = time.time()
    first_tree = TreeNode(10)
    first_tree.left = TreeNode(5,TreeNode(3,TreeNode(3),TreeNode(-2)),TreeNode(2,None,TreeNode(1)))
    first_tree.right = TreeNode(-3,None,TreeNode(11))
   

    print(f'\nThe First tree looks [10,5,-3,3,2,null,11,3,-2,null,1]\n')  
    num1 = 8
    res1 = founder.findingSum(first_tree,num1)
    print(f'Our target Sum:{num1} ==> How many? {res1}\n')
# root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 ==> 3
    sec_tree = TreeNode(5)
    sec_tree.left = TreeNode(4,TreeNode(11,TreeNode(7),TreeNode(2)),None)
    sec_tree.right = TreeNode(8,TreeNode(13,TreeNode(5),TreeNode(1)),TreeNode(4))
    
    print(f'\nThe Second tree looks [5,4,8,11,null,13,4,7,2,null,null,5,1]\n')  
    num2 = 22
    res2 = founder.findingSum(sec_tree,num2)
    print(f'Our target Sum:{num2} ==> How many? {res2}\n')

    arrived = time.time()
    print(f'\n\n\tTotal Time: {arrived-going:.5f} Seconds!')


'''

import time

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class pathSumthree437:
    def findingSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0

        # 모든 가능한 경로를 찾는 함수
        def dfs(each_node, each_sum):
            if not each_node:
                return 0
            each_sum += each_node.val
            return (each_sum == targetSum) + dfs(each_node.left, each_sum) + dfs(each_node.right, each_sum)

        # 현재 노드를 시작점으로 하여 dfs를 호출하고, 왼쪽 및 오른쪽 자식에서도 같은 함수를 호출
        return dfs(root, 0) + self.findingSum(root.left, targetSum) + self.findingSum(root.right, targetSum)

# 테스트 코드
if __name__ == "__main__":
    founder = pathSumthree437()
    start_time = time.time()
    
    first_tree = TreeNode(10)
    first_tree.left = TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1)))
    first_tree.right = TreeNode(-3, None, TreeNode(11))
    
    print(f'\nThe First tree looks [10,5,-3,3,2,null,11,3,-2,null,1]\n')  
    result1 = founder.findingSum(first_tree, 8)
    print(f'Target Sum: {8} ==> Number of paths: {result1}\n')
    
    sec_tree = TreeNode(5)
    sec_tree.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None)
    sec_tree.right = TreeNode(8, TreeNode(13, TreeNode(5), TreeNode(1)), TreeNode(4))
    
    print(f'\nThe Second tree looks [5,4,8,11,null,13,4,7,2,null,null,5,1]\n')  
    result2 = founder.findingSum(sec_tree, 22)
    print(f'Target Sum: {22} ==> Number of paths: {result2}\n')
    
    end_time = time.time()
    print(f'\n\n\tTotal Time: {end_time - start_time:.5f} Seconds!')

'''