#program to demonstrate Exception Handling

try:
    names=["nikhil","kumar","klu"]
    #print(names[2])
    print(names[5])
except IndexError as e:
    print(e)
