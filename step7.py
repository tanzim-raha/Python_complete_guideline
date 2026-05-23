#set and function
s={1,2,3,4,5,6,7,8,9}
print(s)
#Remove duplicate value autometicaly.
t={1,2,3,3,3,3,3,3,4,4,4,4,4,5,6,7,8,9}
print(t)

#set doesn't follow indexing
# set is mutable:
"""Add and remove """
s.add(12)
print(s)
t.remove(3)
print(t)
#Union
"""Adds all the unique elements of two sets together."""
print(s|t)
#Intersection:
"""Find the common element of two sets"""
print(s&t)
#Difference
"""Returns a value that is in one set but not in another set."""
print(s-t)
#Symmetric Difference
"""Gives those that are not common"""
print(s^t)




