def fib_rec(r):
    if r == 0:
        return 0
    if r == 1:
        return 1
    
    elif r==2:
        return fib_rec (r - 2) + fib_rec (r - 1)
        
print(list(map(fib_rec, range(1-9))))