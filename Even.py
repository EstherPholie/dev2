def is_even(x):
    return x %2 ==0
numbers = [1,56,234,87,4,76,24,69,90,135]
print(list(filter(is_even,numbers)))
print(list( map(is_even,numbers)))

f1=lambda x:x%2==0
print(list(filter(f1, numbers)))
               
   
import functools
from functools import reduce


   
   
   
   
   
   
     #recursive codes   
#def factorial (num):
    #"""calls for factorials"""
    #if num == 1:
        #return 1
    #else:
        #return num * factorial(num - 1)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n - 1)
    
print (factorial(4))
    
    
    
    
s=["hello", "my", "name", "is", "Sam"]
length = [len(word for word in words]
          tuple (zip(word, length)
