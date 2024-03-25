def getMex(arr):
    mex=0
    for i in range(max(arr)+2):
        found=False
        index=0
        while found==False and index<len(arr):
            if i in arr:
                found=True
            index+=1
        if found==False:
            mex=i
            break
    return mex

# arr=[0,1,2,3,4,5]
# print(getMex(arr))

def finalArray(arr):
    newArr=[]
    for el in arr: #     [1,2,3]0 [0,1,3]2  [0,2,2,3,4]1
        i=el
        unique=False
        while  unique==False and i>=0:
            if el-i not in newArr:
                unique=True
                newArr.append(el-i)
            i-=1

        if unique==False: #masih ambigu
            newArr.append(0)
    return newArr

# print(finalArray(arr))
def getMaxMex(arr):
    newArr= finalArray(arr)
    return getMex(newArr)

# arr=[3,2,3] # mex=0  [0,2,3] mex=1 [0,1,3] m=2 [0,1,2] m=3
# arr=[1,2,2]
arr=[0,0]

print(getMaxMex(arr))


