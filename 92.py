#program to demonstrate csv file handling-7(write data into existing csv file)

import csv
with open("demo1.csv","a",newline="")as fileobj:
    writerobj=csv.writer(fileobj)
    writerobj.writerow([3,"charan",1111.50])
    writerobj.writerow([4,"nithya",4000])

print("Write operation done successfully.....!")
