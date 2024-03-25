import time

def gainMaxValue(security_val, k):
    # Write your code here
    maximal=0
    first=True #
    # arr=list() 
    for i in range(len(security_val)): #len=6 i=1 i=2
        count=security_val[i] # 5 2
        for j in range(i+k,len(security_val),k): # j=3 j=6,j=4 j=7
            count+=security_val[j]  # count = 5+(-8), 2+(-6)=-4
        
        # arr.append(int(count))

        if first==True: # false
            first=False
            maximal=count


        if maximal<count: # -3 < -3  , -3 < -4
            maximal=count
    return maximal
    # return max(arr)

# arr=[2,4,3,5,6,-1,7]
# arr=[3,5,-2,-4,9,16]
# k=2
arr=[5,2,5,-8,-6,-7] #-3 -4 -2 -8 -6 -7
k=3

start=time.time()
print(gainMaxValue(arr,k))
end=time.time()
print(end-start)


# test=[1,2,3,4]
# test=[-1,-2,-3,-4]
# print(max(test))
