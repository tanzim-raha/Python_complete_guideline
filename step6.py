"""A tuple is a collection of items like a list 📦
But the main difference is: use()

👉 Tuple cannot be changed after creation
This is called immutable.
✅ Ordered
✅ Allows duplicate values
✅ Can store different data types
❌ Cannot add/remove/change items"""

tuple1=("tanzim",20,True)
print(tuple1)
#Accessing Tuple Items
print(tuple1[0])
#count tuple one specific item
nums = (1, 2, 2, 3,1,1,1,1)

print(nums.count(1))
#len check
print(len(nums))

#dictionary
"""A dictionary stores data in key : value pairs 🔑
Think like:
Student ID → Student Name
Country → Capital
Username → Password"""

"""✅ Stores data as key-value pairs
✅ Mutable (can change data)
✅ Fast searching
✅ Keys must be unique
✅ Uses { }"""

student = {
    "name": "Tanzim",
    "age": 20,
    "dept": "CIS"
}

print(student["name"])
#Changing Values
student["age"] = 21
print(student["age"])

#Adding New Data
student["cgpa"] = 3.80
#Removing Data
student.pop("age")

print(student)