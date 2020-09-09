# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    # Empty array to insert merged values into :)
    merged_arr = []

    # Your code here
    
    # Starging index for arrA and arrB
    index_a = 0
    index_b = 0

    # Loop until it has gone through all numbers in arrA and arrB
    while index_a < len(arrA) and index_b < len(arrB):
        # Check if the current a index value is greater than current B index value 
        if arrA[index_a] < arrB[index_b]:
            # Appends the value to the merged array
            merged_arr.append(arrA[index_a])
            # Increases a index
            index_a += 1
        else:
            # Same but for b :)
            merged_arr.append(arrB[index_b])
            index_b += 1

    # If we've gone through all elements in A then we can merge the 
    # rest of the elements in B
    if index_a is len(arrA): 
        merged_arr.extend(arrB[index_b:])
    else:
    # Same principle :) 
        merged_arr.extend(arrA[index_a:])

    # Returns merged array
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively

def merge_sort(arr):
    # Your code here

    # there is nothing to sort
    if len(arr) <= 1:
        return arr

    # Recursively passes down the items to the left of the middle
    left = merge_sort(arr[:len(arr) // 2])
    # Same but for the right :) 
    right = merge_sort(arr[len(arr) // 2 :] )

    # Merges left and right
    return merge(left, right)
        

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
