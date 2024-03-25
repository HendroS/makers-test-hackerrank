import math
def factors(n,p):

    arr=[]
    index2=0
    for i in range(1,n+1):
        if n%i==0:
            index2+=1
            arr.append(i)
            if index2==p:
                print(i)
                break
    arr1=[]
    arr2=[]
    index=0
    print(arr)
    for i in range(1,math.ceil(n/2)):
        if n%i==0:
            index+=1
            if index==p:
                    print(arr1+arr2)
                    return i
            elif arr1==[] or i<arr2[0]:
                # index+=1
                arr1.append(i)
                if i != int(n/i):
                    arr2=[int(n/i)]+arr2
            else:
                break

    # print(arr)
    print(arr1+arr2)
    # print(arr2)
    if p-index>len(arr2):
        return 0
    return arr2[p-1-index]

n=20
p=200
import time
t1=time.time()
print(factors(n,p))
t2=time.time()
print(t2-t1)