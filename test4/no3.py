import calendar
def preprocessDate(dates):
    # Write your code here
    # month={
    #     'Jan':1,
    #     'Feb':2,
    #     'Mar':3,
    #     'Apr':4,
    #     'May':5,
    #     'Jun':6,
    #     'Jul':7,
    #     'Aug':8,
    #     'Sep':9,
    #     'Oct':10,
    #     'Nop':11,
    #     'Dec':12
    # }

    pass


# d=[]
# print(preprocessDate())
arr=[]
d=dict()
i=0
for m in calendar.month_name:
    # arr.append((m[:3],i))
    if m!="":
        if i<10:
            d[m[:3]]=f'0{i}'
        else:
            d[m[:3]]=f'{i}'
    i+=1
# arr.pop(0)
print(d)

s="20th Oct 2052"
s=s.split(" ")
print(s[0][:-2])

