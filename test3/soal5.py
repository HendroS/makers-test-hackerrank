arr=[5,3,2,4,1,2]

arr=sorted(arr)
arr2=[]

for i in range(1,len(arr)+1):
    print(arr[-i:],arr[:-i])

print(arr)