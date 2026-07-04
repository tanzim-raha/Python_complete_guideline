"""Linear Search
Algorithm
Start from the first element.
Compare the current element with the target value.
If they are equal, return the index.
Otherwise, move to the next element.
If the end of the list is reached without finding the target, return -1.
"""
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1

arr = [10, 15, 20, 25, 30, 35, 40, 45, 50]
x = 45

r = search(arr, x)

if r != -1:
    print("Element found at index:", r)
else:
    print("Element not found")