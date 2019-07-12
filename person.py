def get_age():
    age=int(input("Enter your age"))
    return age

def get_name():
    name=input("Enter your name")
    print(name)
    return name

    

myage = get_age()

myname=get_name()

print("my name is %s !" % myname)
print("my age is %d !" % myage)
print("my name is %s and my age is %d!" % (myname, myage))
