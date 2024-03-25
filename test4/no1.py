def minimalOperations(words):
    # Write your code here
    arr=[]
    for el in words:
        # for i in(1,len(el)-1):
        i=1
        change=0
        while i<len(el):
            if el[i-1]==el[i]:
                change+=1
                if i+1<len(el):
                    if el[i]==el[i+1]:
                        i+=1
                # if el[i]==el[i+1]:
                #     i+=1
            i+=1
        arr.append(change)
    return arr

s=['ab','aab','abb','abab','abaaaba']
#01101
print(minimalOperations(s))