# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return - 1
    mid = start + (end - start) // 2
    if target is arr[mid]:
        return mid
    elif target <= arr[mid]:
        return binary_search(arr, target, start, mid -1)
    else:
        return binary_search(arr, target, start, end + 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8]



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

