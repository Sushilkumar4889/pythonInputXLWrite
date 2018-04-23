#Create multiple excel sheet according to the user and store the data in particular sheet.
#example format of data input will be like ("first letter of sheet", data); eg (h,24) here "h" will denote the sheet location on which sheet data will be stored

import xlwt,xlrd
wb = xlwt.Workbook()


sheet= int(input("no. of sheet"))

for i in range(0,sheet):
    name= input("sheet name")

    ws = wb.add_sheet(name)
    

r = int(input("row"))
c = int(input("col"))
val = input("enter data (location,data)  ")
print (val)
print (type(val))
val=val.split(",")
print (val)
print (type(val))

try:
    val=int(val)
except:
    pass
if val[0][0]==ws[0]:
    
    ws.write(r,c,val[1])

wb.save("first.xls")

