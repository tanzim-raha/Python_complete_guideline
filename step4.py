#Loop
"""    For Loop     """
"""       range(start,end,step[difference])                  """

for x in range(10): # end = n-1 = 10-1 = 9( start =0)
    print(x, "end")     #output= 0 1 2 3 4 5 6 7 8 9
    
for y in range(2,6): #end=n-1= 6-1   start=2
    print(y)
    
for z in range(1,30,3):#start=1 end=n-1 =30-1=29  step=3(1..4..7.............) 
    print(z)           #3 kore difference takbe sobar maje 4-1=3 ,7-4=3 ......continue

"""     while loop     """
num=1
end=11  # end is always n-1 time happen 
while num<end:
    print(num)
    num+=1 # if we dont use this line output become nonstop 1 (nonstop infinite loop)
    
"""Ex 1"""

T= 1

while T <= 5:
    print(T)
    T += 1

#Print Even Numbers
R = 2

while R <= 10:
    print("Even number:",R)
    R += 2
#Print Odd Numbers
F=1

while F <=10:
    print("ODD number",F)
    F +=2
#Countdown Example
e=5

while e >0:
    print(e)
    e-=1   # its create the decrement values
    

#. Multiplication Table of 3

q=1

while q<=10:
    print("3 * ",q," = ",3*q)
    q+=1 # this line ensure the increment of q value one 
            #loop end and increment the value and again start next loop
#Sum of Numbers

num = 1
total = 0

while num <= 5:
    total += num
    num += 1

print("Total =", total)

# multiply:
w=1
to=1
    
while w<=5:
    to*=w
    w+=1
    print("m=",to)
    
print("m=",to)

#Break Example

num = 1

while True:
    print(num)
    
    if num == 5:
        break
    
    num += 1
    
#continue ex:
num = 1

while True:
    print("my ",num)
    
    if num == 9:
        break
    
    num += 1