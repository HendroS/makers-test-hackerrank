#solved
from datetime import datetime
def extractErrorLogs(logs:list):
  

    for el in logs.copy():
        if el[2] !="ERROR" and el[2] !="CRITICAL":
            logs.remove(el)
  
    # logs.sort(key=lambda date:datetime.strptime(date[0],'%m-%d-%Y'))
    logs.sort(key=getdate)

 
    return logs
    
def getdate(a):
    time= a[0]+' '+a[1]
    return datetime.strptime(time,"%d-%m-%Y %H:%M")

arr=[
    ['10-20-2018',1,"INFO"],
    ['10-20-2018',2,"ERROR"],
    ['10-20-2017',3,"ERROR"],
    ['10-20-2018',7,"CRITICAL"],
    ['10-20-2018',4,"INFO"],
    ['10-20-2019',5,"INFO"],
    ['10-20-2019',6,"CRITICAL"],
     ]

# print(datetime.strptime(arr[0][0],'%m-%d-%Y'))
# print(getdate(arr[0]))

# print(extractErrorLogs(arr))


# arr=[1,2,3,4,5,3]
# while 3 in arr:
#     arr.remove(3)
#     print('hapus')


# for i in arr:
#     if i == 3:
#         arr.remove(i)
#         # arr.insert(i,'x')
#         print('remove')
# print(arr)

# def compare(a, b):
#     return (True-False)

# print(compare('a','b'))
# dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
# print(dt)

a=[
    ['21-01-2022','18:00','CRITICAL'],
   ['01-01-2023','15:00','ERROR'],
   ['01-01-2023','16:00','SUCCESS']
   ]
# time= a[0][0]+' '+a[0][1]
# print(time)
# print(datetime.strptime(time,"%d-%m-%Y %H:%M"))
print(extractErrorLogs(a))