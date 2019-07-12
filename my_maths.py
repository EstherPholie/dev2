def calculate(operation, a,b):
    print(operation, a, b)
    if (operation=="multiply"):
        return (a*b)
    if (operation=="add"):
        return (a+b)
    if (operation=="divide"):
        return (a/b)
    if (operation=="subtract"):
        return (a-b)
    
    
x = calculate("add",3, 4)
print(x)

x = calculate("multiply",3, 4)
print(x)

x = calculate("divide",3, 4)
print(x)

x = calculate("subtract",3, 4)
print(x)