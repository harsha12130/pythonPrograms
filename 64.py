#program to demostrate Exception Handling

try:
    name="KLUNIVERSITY" #group of characters
    print("Name Length:",len(name))
    #print(name[2]) #3rd Character
    #print(name[15])
    #print(nae[1:10:2])
    print(name[::-1])
except:
    print("Exception Ocurred")
