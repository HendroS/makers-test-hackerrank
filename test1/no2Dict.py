def countPairs(projectCosts, target):
    # Write your code here
    
    diction=dict()
    c=0
    # setP=list(set(projectCosts))
    # for x in setP:
    #     diction[x]=projectCosts.count(x)
    # for p in setP:
    #     if p-target in diction: #-3 -1 1 3 5 7
    #         c+=diction[p-target]  #c=1 c=2 c=3 c=4
            
    #     if p+target in diction: #3 5 7 9 11
    #         c+=diction[p+target]
    
    for p in projectCosts: #-1 1 3 5 7 9
        if p-target in diction: #-3 -1 1 3 5 7
            c+=diction[p-target]  #c=1 c=2 c=3 c=4
            
        if p+target in diction: #3 5 7 9 11
            c+=diction[p+target]
        diction[p]=diction.get(p,0)+1 #dict{-1:1 1:1,3:1,5:1, 7:1, 9:1}
        # print(diction[p])
    print(diction)
    return c
    # return diction

p=[1,1,3,5,5,7,9]
k=2
print(countPairs(p,k))
