"""Recursion means:
a recursive function is a function that calls itself 
again and again until a stopping condition is met."""
"""A recursive function has 2 parts:
1. Base Case 🛑 Stops recursion.
2. Recursive Case 🔄Function calls itself with a smaller/simpler problem."""
def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
    
show(5)
#Factorial Calculation
def fact(n):
    if n==1:
        return 1
    return n* fact(n-1)

print("factorial=",fact(5))
#Fibonacci Series
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
for i in range(10):
    print(fib(i))
    




