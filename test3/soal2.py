def findL(arr):
    matrix=len(arr)
    
    while matrix>0:
        # print('m=',matrix)
        for baris in range(len(arr)+1-matrix):
            # defect=False
            for kolom in range(len(arr)-matrix+1):
                arr2=[]
                for el in arr[baris:baris+matrix]:
                    defect=False
                    # arr2.append(el[kolom:kolom+matrix])
                    # print(el[kolom:kolom+matrix])
                    if 0 in el[kolom:kolom+matrix]:  
                        defect=True
                        # arr2=[]
                        break
                        
                # print('defect= ',defect)
                if defect==False:
                    # for el in arr2:
                    #     print(el)
                    return matrix
                # print('=============')

            
                
            # print('matrix baris ke-',baris)
            # print('----------')
    
        matrix-=1

    return matrix

# arr=[
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,0,0,0]]
arr=[
    [1,1,0,1],
    [1,0,1,1],
    [1,1,0,1],
    [1,0,1,1]]
print('max matrix=', findL(arr))
