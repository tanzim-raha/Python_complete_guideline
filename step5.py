#List =[ values ]
"""Store many values together
Keep data in order
Store different types of data at once
Add new items
Remove items
Change existing items
Find specific items
Count items
Sort data
Reverse data order
Repeat data
Combine multiple lists
Loop through data one by one
Store nested data (list inside list)"""

#Ex1:
my_list=[1,2,3,4,5,6,7,]

print(my_list)

#ex2:
fruit=["mango","jackfruit","berry","banana"]

print(fruit)

#ex3:
list1=[1,2,9,1.5,"hello",3,9]
print(list1)

#list indexing
list2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#list2=[0,1,2,3,4,5,6,7,8,-----------------------------,19]
print(list2[2])
print(list2[-1])#counting list from last
#Count Items
print(len(list2))
#sorted list
list3=[1,4,3,6,7,4,9,2,3,0,13]
list3.sort()
print(list3)
#List Insert(add)
#append()
list4=[11,22,33,44,55,66,77,88,99]
list4.append(31) #append function added value in the last position of list
print(list4)
"""If we want to added value in our 
choose position we have to use insert()function"""
#ex:
list5=[1,2,3,4,5,6,7,8,9]
list5.insert(2,33)#insert(position,value)
print(list5)
"""If we add 2 list or extended then 
we have to use extend function"""
#list_name1.extend(list_name2)
list4.extend(list5)# print first list4 then list5
print(list4)
#List Delete(remove)
list6=["r","a","h","a","r"]
list6.remove("r")#delete just front index value if there was multiple value in the list
print(list6)
#pop() Deletes the item according to the index.
list7=[1,2,"u","q","s"]
list7.pop(1)
list7.pop(-1)
print(list7)
#del
list8=["b","a","n","a","n","a"]
del list8[0]
print(list8)

#clear()
list8.clear()
print(list8)



"""List comprehension:
it is a shortcut method for creating a list on one line."""

"""[new_item for item in collection] 
item will come from collection one by one new_item will be stored in list"""

number=[x for x in range(5)]
print(number)

#Square Numbers
squares = [x*x for x in range(5)]

print(squares)

#With Condition
even = [x for x in range(10) if x % 2 == 0]

print(even)

#Convert to Uppercase

names = ["rahima","rahim"]

upper = [x.upper() for x in names]

print(upper)