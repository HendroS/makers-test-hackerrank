import itertools
import time
def countPairs(projectCosts, target):
    # Write your code here
    #[1,2,3] 1 sama 2 selisih sama dengan target? 
    #[1,2,3]
    #[1,2,3]
    count=0
    for x,y in itertools.combinations(projectCosts,2):
        if abs(x-y)==target:
            count+=1
    # count= [(x,y) for x,y in itertools.combinations(projectCosts,2) if abs(x-y)==target]
    # for i in range(len(projectCosts)-1): 
    #     for j in range(i+1,len(projectCosts)):
    #         print(projectCosts[i],projectCosts[j])
    #         if abs(projectCosts[i]-projectCosts[j])==target:
    #             count+=1
    #             print([projectCosts[i],projectCosts[j]])

    
    return count

projectCostsprojectCosts=[1,1,2,3,4]
target=2
start=time.time()
print(countPairs(projectCostsprojectCosts,target))
print(time.time()-start)