def sortByVal(arr:[str]):
    d=dict()
    for el in arr:
        temp=el.split(" ")
    
        if el.split(" ")[0] in d:
            d[temp[0]]+=1
        else:
            d[temp[0]]=1
        if el.split(" ")[1] in d:
            d[temp[1]]+=1
        else:
            d[temp[1]]=1
    for k in d:
        print(k,d[k])
    print(d.items())
    d=dict(sorted(d.items(),key=lambda x:(-x[1],x[0]),reverse=False))
    print("___________________")
    for k in d:
        print(k,d[k])   
    



arr=["89 88 2000","88 89 1000","2 23 1000","1 2 3000","3 10 4000",
     "90 73 3000","77 90 4000"]

sortByVal(arr)
