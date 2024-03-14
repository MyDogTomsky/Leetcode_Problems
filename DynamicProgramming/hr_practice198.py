import time
import os

def epic_way(village):
    
    n = len(village)
    dp = [0] * n
    dp[0] = village[0]
    dp[1] = max(village[0],village[1])
    dp[2] = max(dp[0]+village[2],village[1])
    for i in range(3,n):
        dp[i] = max(dp[i-3]+village[i-1],dp[i-2]+village[i])

    return dp[n-1]    

start_time = time.time()


print(f'\n\nWorking Directory: {os.getcwd()}')

village_1 = [1,2,3,1]
village_2 = [2,7,9,3,1]

village_set = [village_1]
village_set.append(village_2)

for each_village in village_set:
    sel_way = epic_way(each_village)
    print(f'\nWhen this case: {each_village} is robbed, the biggest money should be {sel_way}\n')



end_time = time.time()
print(f'\n\n{end_time - start_time:.4f}has consumed. It is reported to the server.\n')