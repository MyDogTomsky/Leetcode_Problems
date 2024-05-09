# Leetcode 437_using HashMap

# root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8   ==> 3
# root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 ==> 3
# starting point doesn't need to be from the first root!
# all the fruits have no need to connect each other!

import time

class TreeNode:
    def __init__(self,val = 0, left= None,right = None):
        self.val = val
        self.left = left
        self.right = right

class pathSumthree437_2:
    def findingSum(self,root:TreeNode,target_num) -> int:
        from collections import defaultdict
        cumulative = defaultdict(int)
        cumulative[0] = 1

        def dfs(each_node,current_sum):
            if not each_node:
                return 0
            current_sum += each_node.val
            available = cumulative[current_sum-target_num]
            cumulative[current_sum] +=1
            result = available + dfs(each_node.left,current_sum) + dfs(each_node.right,current_sum)
            cumulative[current_sum] -= 1
            return result
        
        return dfs(root,0)
        

if __name__ == "__main__":

    summer = pathSumthree437_2()
    going = time.time()
    tree_first = TreeNode(10)
    tree_first.left = TreeNode(5,TreeNode(3,TreeNode(3),TreeNode(-2)),TreeNode(2,None,TreeNode(1)))
    tree_first.right = TreeNode(-3,None,TreeNode(11))
   

    print(f'\nThe First tree looks [10,5,-3,3,2,null,11,3,-2,null,1]\n')  
    num1 = 8
    res1 = summer.findingSum(tree_first,num1)
    print(f'Our target Sum:{num1} ==> How many? {res1}\n')
# root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 ==> 3
    tree_two = TreeNode(5)
    tree_two.left = TreeNode(4,TreeNode(11,TreeNode(7),TreeNode(2)),None)
    tree_two.right = TreeNode(8,TreeNode(13,TreeNode(5),TreeNode(1)),TreeNode(4))
    
    print(f'\nThe Second tree looks [5,4,8,11,null,13,4,7,2,null,null,5,1]\n')  
    num2 = 22
    res2 = summer.findingSum(tree_two,num2)
    print(f'Our target Sum:{num2} ==> How many? {res2}\n')

    arrived = time.time()
    print(f'\n\n\tTotal Time: {arrived-going:.5f} Seconds!')