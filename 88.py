#program to demonstrate CSv file handling-3(displaying record based on ID)

import csv
with open("demo.csv","r")as fileobj:
    readerobj=csv.reader(fileobj)
    print("***Employee Records***")
    next(readerobj)
    id=int(input("Enter Employee ID:"))
    flag=False
    for row in readerobj:
        if id==int(row[0]):
            print(row[0],row[1],row[2],row[3],row[4])
            flag=True
    if(flag==False):
        print("ID Not Found")
