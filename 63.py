#program to demonstrate Exception Handling

try:
    demo=[10,20,30,40]
    print("Length of Demo List",len(demo))
    #print(demo[2])
    print(demo[5])
except:
    print("Exception Occurred")
