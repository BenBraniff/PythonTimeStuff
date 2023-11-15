import time
from time import sleep

myBirthday = (2004, 5, 14, 0, 0, 0, 0, 0, 0)

print()
print()

for i in range(1):
    
    print("Current date: ", end="")
    print(time.localtime().tm_year, "-", time.localtime().tm_mon, "-", time.localtime().tm_mday)
    print("My birthday in seconds since epoch (i.e. since jan 1, 1970): ", end="")
    print(time.mktime(myBirthday))
    print("My age in seconds since epoch:                               ", end="")
    print(time.time() - time.mktime(myBirthday))
    #when first writing this code I'm 19.515 years old
    print("My current age based of seconds since epoch data:            ", end="")
    myAge = (time.time() - time.mktime(myBirthday))/31536000
    print(round(myAge, 2))

    print("Current time in seconds since epoch:                         ", end="")
    print(time.time())
    #sleep function uses seconds
    #sleep(2)

print()
print()