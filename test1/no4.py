#boosted
def isPossible(a, b, c, d):
    # Write your code here
    # matchA= False
    # matchB=False
    if (a==c or (c-a)%b ==0) and (b == d or (d-b)%c ==0 or ()) :
        return 'Yes'
    # elif a==c or (c-a)%b ==0 :
    #     matchA=True
    # elif (c-a)%b ==0:
    #     # matchA=True
        # if b==d or (d-b)%c ==0:
        #     return 'Yes'
        # return 'No'    
    return 'No'
        
    # if a==c and b == d:
    #     return 'Yes'
    # else:
    #     if a==c:
    #         matchA = True
    #     while matchA==False and a<c:
    #         a=a+b
    #         if a==c:
    #             matchA=True
    #     if matchA:
    #         if b==d:
    #             matchB = True
    #         while matchB==False and b<d:
    #             b=b+a
    #             if b==d:
    #                 matchB = True

    # if matchA==True and matchB==True:
    #     return 'Yes'
    # return 'No'

# print(isPossible(2,3,8,19))
# import time
# start=time.time()
# print(isPossible(2,3,8,19))
# end=time.time()
# print(end-start)
#(1,1)(1,2)(1,3)
#(1,1),(2,1),(2,3),(2,5),(2,7),(2,9)
# print(isPossible(1,2,5,9))  = (5%2) -1 ==0? 
#(1,2),(3,2),(5,2),(5,7),(5,12),(5,17)
# print(isPossible(1,2,1,9))  = (5-1) %2 ==0?    
#(1,2),(3,2),(5,2),(5,7),(5,12),(5,17)

#(1,1,5,11)
# 1,1 2,1 3,1 4,1 5,1   5,6 5,11 5,16  ===   5-1 / 1=4    (d-c)%b 11-5 6%1=0

#(2,3,8,19)
# 2,3  8,9
#2,3 5,3 8,3 8,11 8,19 
# (c-a)%b (8-2)%3=0  6/3=2
# (d-b)%c 


print(isPossible(1,4,62,45))

#(1,4)(5,4)(9 13 17 21 25 29)()
#c=62  d=45  b=4
#(1,5)(1,6)(1,45)(46,45) ()

print([int (x) for x in range(1,70,4)])
