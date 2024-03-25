def kSub(k, nums):
    # Write your code here
    # arr=[]
    # count=0
    # for i in range(len(nums)): #
    #     total=nums[i]
    #     if total % k==0:
    #         count+=1
        
    #     for j in range(i+1,len(nums)):
    #         total+=nums[j]
    #         if total % k==0:
    #             count+=1
    # return count

    sum=0
    diction={0:1}
    result=0
    for x in nums:
        sum=(sum+x)%k
        if sum in diction:
            result+= diction[sum]
            print('sum=',sum,'res=',result)
        
        diction[sum]=diction.get(sum,0)+1
    print(diction)
    return result



arr=[1, 2, 3, 4, 1]
k=5
# arr=[5,10,11,9,5]
# k=5
print(kSub(k,arr))