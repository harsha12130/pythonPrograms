#program to demonstrate Exception Handling
try:
    print("***I am in try block***")
    print("Run this code")
except:
    print("***I am in except block***")
    print("Exception Occurred")
else:
    print("***I am in else block***")
    print("No Exception Occurred")
finally:
    print("***I am in finally block***")
    print("Always Executed")
