#program to demonstrate CSv file handling-5(displaying total salary)

import csv
with open("demo.csv","r")as fileobj:
    readerobj=csv.reader(fileobj)
    next(readerobj)
    totalsal=0.0
    for row in readerobj:
        totalsal=totalsal+float(row[3])
    print("Total salary:",totalsal)
