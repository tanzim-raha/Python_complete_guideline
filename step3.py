#Conditional Statement
"""If statement = runs code if condition is true
If-else statement =chooses between two options
If-elif-else = checks multiple conditions"""

#ex
age=18

if(age>=18):
    print("true")
else:
    print("false")
    
#ex(nested if_else)  

num = 10

if num > 0:
    print("Positive number")

    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number")



