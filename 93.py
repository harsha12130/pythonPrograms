#program to demonstrate csv file handling-8(copying the data from one file to another)

import csv
with open("demo2.csv","w",newline="")as outputfileobj:
    writerobj=csv.writer(outputfileobj)
    with open("demo1.csv","r")as inputfileobj:
        readerobj=csv.reader(inputfileobj)
        for row in readerobj:
            writerobj.writerow(row)

print("Write operation done successfully.....!")
