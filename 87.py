#program to display CSV File handling-2 (displaying rows with index)

import csv
with open("demo.csv","r")as fileobj:
    readerobj=csv.reader(fileobj)
    print("***Employee Records***")
    next(readerobj)
    for row in readerobj:
        print(row[0],row[1],row[2],row[3],row[4])
