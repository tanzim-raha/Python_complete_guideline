"""Function:
Standard Library Functions
:The functions that Python has already created are called Standard Library Functions or Built-in Functions"""
import math
print(pow(2,3))#power value using builtin function 

s_root=math.sqrt(4)#root value using function 

print(s_root)

p=math.sqrt(5)
print(p)

"""User Defined Functions:
Functions that are created by the programmer themselves are called User Defined Functions."""
#The values ​​that are passed inside the function are called arguments.
#ex1:
def greet():
    print("hello")
    
#function call
greet()

#two argument in function:
def add_num(n1,n2):
    total=n1+n2
    print("sum=",total)
add_num(12,13)

#Default Arguments  set up:
def fruit(name="jackfruit"):
    print(name)
    
fruit()
fruit("Mango")
#Keyword Arguments
def student(name,age):
    print(name,age)
    
student(age=20, name="tanzim")#Order is not important.

#Positional Arguments

def info(name,age):
    print(name,age)
    
info("raha",20)#If the position changes, the output will also change.
"""*args is used when it is not known
how many arguments will be received."""

def number1(*nums):
    print(nums)
number1(1,2,3,4,5)#all values ​​are stored as tuples.

def total(*numbers):

    print(sum(numbers))

total(1,2,3,4)
#return is used to send a value out of a function.

def add_number():
    sum=5+8
    return sum

result=add_number()

print(result)

def f_square(num):
    result=num*num
    
    return result

square= f_square(3)
print("s=",square)


def check(num):

    if num % 2 == 0:
        return "Even"

    return "Odd"

print(check(4))
print(check(7))


#nested function
#outer function
def f1():
    
    s="tanzim raha"
    
    # inner function
    
    def f2():
        print(s)
        
    f2()
    
f1()

#Lambda is a single-line function।
# lambda arguments:expression

#ex1:

greet= lambda : print("hello")

greet()

t= lambda:print("123tan123")

t()

"""Lambda with One Argument"""
t_user=lambda name:print("hey there,",name)

t_user("razu")

R=lambda roll:print(roll)
R(12)

#Lambda with Multiple Arguments

x=lambda a,b,c:a+b+c
print(x(2,2,2))

y=lambda a,b:(a*b ,a/b)
print(y(10,5))


